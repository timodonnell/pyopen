import os
import tempfile

TEMPORARY_FILES = []

def tempfile_path(prefix='', suffix=''):
    '''
    Return a path to a new temporary file. The caller is responsible for
    deleting the file when finished.
    '''
    fd = tempfile.NamedTemporaryFile(
            prefix=prefix,
            suffix=suffix,
            delete=False)
    fd.close()
    TEMPORARY_FILES.append(fd.name)
    return fd.name

def finished(delete=True, quiet=False):
    '''
    Print the names of temporary files and delete them if delete=True.

    Call this when the process is finishing.
    '''
    global TEMPORARY_FILES
    for filename in TEMPORARY_FILES:
        if delete:
            if not quiet:
                print("Deleting: %s" % filename)
            os.unlink(filename)
        else:
            if not quiet:
                print("Not deleting: %s" % filename)
        TEMPORARY_FILES = []
