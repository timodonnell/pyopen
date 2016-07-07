from __future__ import absolute_import

from .base import BaseLoader

from six.moves.cPickle import load

class Pickle(BaseLoader):
    name = "pickle"
    extensions = ["pkl", "pickle"]

    @staticmethod
    def add_arguments(parser):
        pass

    @staticmethod
    def load(args, filename):
        with open(filename) as fd:
            return load(fd)

    @staticmethod
    def summarize(obj):
        return str(type(obj))