'''
Utility functions for tests.
'''
import sys
from six import StringIO

from pyopen.command import run

import os

def data_path(name):
    '''
    Return the absolute path to a file in the pyopen/test/data directory.
    The name specified should be relative to pyopen/test/data.
    '''
    return os.path.join(os.path.dirname(__file__), "data", name)

def run_and_capture(code, argv):
    original_stdout = sys.stdout
    try:
        sys.stdout = StringIO()
        run(argv + ["-q", "--code", code])
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdout = original_stdout
