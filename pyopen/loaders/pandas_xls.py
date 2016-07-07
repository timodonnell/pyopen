from __future__ import absolute_import

from .base import BaseLoader

import pandas

class PandasXLS(BaseLoader):
    name = "pandas_xls"
    extensions = ["xls", "xlsx"]

    @staticmethod
    def add_arguments(parser):
        pass

    @staticmethod
    def load(args, filename):
        return pandas.read_excel(filename, sheetname=None)

    @staticmethod
    def summarize(df_dict):
        return "dict of %d data frames: %s" % (
            len(df_dict), ", ".join(str(x) for x in df_dict))