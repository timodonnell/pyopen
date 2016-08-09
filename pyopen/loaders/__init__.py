from __future__ import absolute_import

import collections

from . import pandas_csv, pandas_xls, json, pickle, text

LOADERS = collections.OrderedDict((loader.name, loader) for loader in
    [
        pandas_csv.PandasCSV,
        pandas_xls.PandasXLS,
        json.JSON,
        pickle.Pickle,
        text.Text,
])

__all__ = [
    "pandas_csv",
    "pandas_xls",
    "json",
    "pickle",
    "text",
]
