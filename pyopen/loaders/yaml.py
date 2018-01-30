from __future__ import absolute_import

from .base import BaseLoader

import yaml

class Yaml(BaseLoader):
    name = "yaml"
    extensions = ["yaml", "yml"]

    @staticmethod
    def add_arguments(parser):
        pass

    @staticmethod
    def load(args, filename):
        with open(filename) as fd:
            return yaml.load(fd)

    @staticmethod
    def summarize(obj):
        return str(type(obj))
