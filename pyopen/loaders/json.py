from __future__ import absolute_import

from .base import BaseLoader

import json

class JSON(BaseLoader):
    name = "json"
    extensions = ["json"]

    @staticmethod
    def add_arguments(parser):
        pass

    @staticmethod
    def load(args, filename):
        with open(filename) as fd:
            return json.load(fd)

    @staticmethod
    def summarize(obj):
        return str(type(obj))