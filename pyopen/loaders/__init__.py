from __future__ import absolute_import

import collections

from . import pandas_csv, pandas_hdf5, pandas_xls, json, yaml, pickle, text

LOADERS = collections.OrderedDict((loader.name, loader) for loader in
    [
        pandas_csv.PandasCSV,
        pandas_xls.PandasXLS,
        pandas_hdf5.PandasHDF5,
        json.JSON,
        yaml.Yaml,
        pickle.Pickle,
        text.Text,
])

__all__ = [
    "pandas_csv",
    "pandas_xls",
    "pandas_hdf5",
    "json",
    "yaml",
    "pickle",
    "text",
]
