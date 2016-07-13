pyopen
======

pyopen is a command-line tool for quickly inspecting files using python. It drops you into an interactive IPython session with the parsed files available as local variables.

Currently supports csv/tsv files (uses pandas and also supports gzip / bz2 compression), excel, json, and pickle files. We welcome contributions of loaders for other file types.

Installation
-------------
::

    pip install pyopen

To run the tests:

::

    nosetests

Example
-------------

::
    $ pyopen test/data/data1.csv

    f1 test/data/data1.csv 4.9 kB pandas_csv

    Python 2.7.10 (default, May 26 2015, 13:01:57)
    Type "copyright", "credits" or "license" for more information.

    IPython 4.0.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.
    1 files loaded:

    f1 test/data/data1.csv 4.9 kB pandas_csv
        pandas.DataFrame: 99 rows x 8 cols.
        Columns: patient genome contig interbase_start interbase_end ref alt validation

    Variables defined:
        f1 : the parsed file
        loaded : object with attributes for each parsed file (abbreviated filenames, tab completes)
        loaded_filenames : dict from filename to parsed file
        loaded_absolute_filenames : dict from absolute filename to parsed file
        loaded_list : list of the parsed files

    To print this message again later, type 'info()'. To quit type 'quit()'.

The variable 'f1' is a pandas DataFrame with the contents of the csv file:

::

    In [1]: f1.head()
    Out[1]:
      patient  genome contig  interbase_start  interbase_end ref alt validation
    0     PT1  GRCh37   chr1         10719783       10719784   T   G   untested
    1     PT1  GRCh37   chr1         11137693       11137694   G   A   verified
    2     PT1  GRCh37   chr1         11826130       11826131   A   T   verified
    3     PT1  GRCh37   chr1         17664605       17664606   C   G   verified
    4     PT1  GRCh37   chr1         26670492       26670493   G   T   verified


