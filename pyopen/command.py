'''
Launch an ipython session with the specified files parsed and available as
variables 'f1', 'f2', etc.

'''

import sys
import argparse
import collections
import os

from six import exec_

import IPython
from traitlets.config import Config

import humanize

import loaders
from . import load

parser = argparse.ArgumentParser(description=__doc__)

parser.add_argument("files", nargs="*", metavar="FILENAME",
    help="Path to files to open. They will be named f1, f2, etc.")

parser.add_argument("--loader", action="append",
    help="Loader to use. Specify one argument per file. Available loaders: %s"
    % ','.join(sorted(loaders.LOADERS)))
parser.add_argument("--quiet", "-q", action="store_true")
parser.add_argument("--code", action="append",
    help="Instead of launching ipython, just run the given python code.")

for loader in loaders.LOADERS.values():
    group = parser.add_argument_group(title=loader.name)
    loader.add_arguments(group)

def run(argv=sys.argv[1:]):
    args = parser.parse_args(argv)

    loaders_to_use = [
        load.get_loader(
            args.files[i],
            loader_name=None if not args.loader else args.loader[i])
        for i in range(len(args.files))
    ]

    if len(loaders_to_use) != len(args.files):
        raise ValueError(
            "Number files (%d) != number of loaders specified (%d)" % (
                len(args.files), len(loaders_to_use)))

    loaded_filenames = {}
    loaded_absolute_filenames = {}
    loaded_list = []
    all_summary_lines = []
    num_abbreviations = collections.OrderedDict()
    for (i, (filename, loader)) in (
            enumerate(zip(args.files, loaders_to_use))):

        loaded_file = loader.load(args, filename)
        num_abbreviation = "f%d" % (i + 1)

        loaded_filenames[filename] = loaded_file
        loaded_absolute_filenames[os.path.abspath(filename)] = loaded_file
        loaded_list.append(loaded_file)
        num_abbreviations[num_abbreviation] = loaded_file

        summary_lines = []

        summary_lines.append("%s %s %s %s" % (
            num_abbreviation,
            filename,
            humanize.naturalsize(os.stat(filename).st_size),
            loader.name))
        summary_lines.append(
            "\t" + "\n\t".join(loader.summarize(loaded_file).split("\n")))
        summary_lines.append("")
        all_summary_lines.extend(summary_lines)

        if not args.quiet:
            print(summary_lines[0])

    if not args.quiet:
        print("")

    def info():
        print("%d files loaded: \n" % len(args.files))
        for line in all_summary_lines:
            print(line)

        print("Variables defined:")
        print("\t%s : the parsed file%s" % (
            ", ".join(num_abbreviations),
            "" if len(num_abbreviations) == 1 else "s"))
        print("\tloaded_filenames : dict from filename to parsed file")
        print(
            "\tloaded_absolute_filenames : dict from absolute filename to "
            "parsed file")
        print("\tloaded_list : list of the parsed files")

        print("\nTo print this message again later, type 'info()'. "
            "To quit type 'quit()'.")

    variables = {
        'loaded_filenames': loaded_filenames,
        'loaded_absolute_filenames': loaded_absolute_filenames,
        'loaded_list': loaded_list,
        'info': info,
    }
    variables.update(num_abbreviations)

    if args.code:
        # Just run the code, no IPython
        for code in args.code:
            exec_(code, variables)
    else:
        config = Config()
        if not args.quiet:
            config.InteractiveShellApp.exec_lines = [
                "info()"
            ]
        config.TerminalIPythonApp.display_banner = not args.quiet

        IPython.start_ipython(argv=[], config=config, user_ns=variables)
