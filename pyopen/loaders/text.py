from __future__ import absolute_import

from .base import BaseLoader

class Text(BaseLoader):
    name = "text"
    extensions = ["txt"]

    @staticmethod
    def add_arguments(parser):
        pass

    @staticmethod
    def load(args, filename):
        with open(filename) as fd:
            return fd.read()

    @staticmethod
    def summarize(obj, max_length=30):
        if len(obj) > max_length:
            value = "%s [...]" % (obj[:max_length])
        else:
            value = obj
        return "Text of length %d: %s" % (len(obj), value)
