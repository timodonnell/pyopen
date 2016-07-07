from __future__ import absolute_import

from .base import BaseLoader

import pandas

def maybe_none(s):
    if s == "none":
        return None
    return s

class PandasCSV(BaseLoader):
    '''
    Loader for CSV and TSV files.
    '''
    name = "pandas_csv"
    csv_extensions = ["csv", "csv.bz2", "csv.gz"]
    tsv_extensions = ["tsv", "tsv.bz2", "tsv.gz"]
    extensions = csv_extensions + tsv_extensions

    @staticmethod
    def add_arguments(parser):
        parser.add_argument("--csv-delimiter", default="by_extension")
        parser.add_argument("--csv-no-header",
            action="store_true",
            default=False)
        parser.add_argument("--csv-names", default=None, nargs="+")
        parser.add_argument("--csv-index-col", default=None, type=int)
        parser.add_argument("--csv-compression",
            default='infer',
            choices={'infer', 'gzip', 'bz2', 'zip', 'xz', 'none'})
        parser.add_argument("--csv-comment", default=None)
        parser.add_argument("--csv-encoding", default=None)

    @classmethod
    def load(cls, args, filename):
        sep = maybe_none(args.csv_delimiter)
        if sep == "by_extension":
            if any(filename.endswith(x) for x in cls.tsv_extensions):
                sep = "\t"
            else:
                sep = ","

        return pandas.read_csv(
            filename,
            sep=sep,
            names=args.csv_names,
            header=(
                'infer' if args.csv_names is None and not args.csv_no_header
                else None),
            index_col=args.csv_index_col,
            compression=(
                None if args.csv_compression == "none"
                else args.csv_compression),
            comment=args.csv_comment,
            encoding=args.csv_encoding)

    @staticmethod
    def summarize(df):
        assert isinstance(df, pandas.DataFrame)
        return "pandas.DataFrame: %d rows x %d cols.\nColumns: %s" % (
            df.shape[0], df.shape[1], " ".join(str(x) for x in df.columns))



