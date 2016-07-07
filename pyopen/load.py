import logging

from .loaders import LOADERS

def get_loader(filename, loader_name=None):
    if loader_name is not None:
        try:
            return LOADERS[loader_name]
        except KeyError:
            raise KeyError("No such loader: %s. Valid loaders are: %s" % (
                loader_name, " ".join(LOADERS)))
    matching = [
        loader for loader in LOADERS.values() if loader.matches(filename)
    ]
    if not matching:
        raise ValueError(
            "No loaders were guessed for file: %s. "
            "Try explicitly specifying one of these loaders: %s" % (
                filename,
                " ".join(LOADERS)))

    loader = matching[0]
    if len(matching) > 1:
        logging.info(
            "Using loader %s for file %s. Other matching loaders: %s" % (
                loader.name,
                filename,
                " ".join(matching[1:])))
    return loader

def load_from_args(filename, args, loader_name=None):
    loader = get_loader(filename, loader_name=loader_name)
    return loader.load(args, filename)
