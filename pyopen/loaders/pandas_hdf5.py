from __future__ import absolute_import

from .base import BaseLoader

import pandas

class PandasHDF5(BaseLoader):
    name = "pandas_hdf5"
    extensions = ["hdf5", "h5"]

    @staticmethod
    def add_arguments(parser):
        pass

    @staticmethod
    def load(args, filename):
        return pandas.HDFStore(filename)

    @staticmethod
    def summarize(obj):
        return str(obj)

