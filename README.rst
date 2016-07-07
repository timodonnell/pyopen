pyopen
======

pyopen is a command-line tool for quickly inspecting files using python. It drops you into an interactive IPython session with the parsed files available as local variables.

Currently supports csv/tsv files (uses pandas and also supports gzip / bz2 compression), excel, json, and pickle files. We welcome contributions of loaders for other file types.

Example
-------------

::

    $ pyopen test/data/SampleCSVFile_11kb.csv --no-header

    f1 test/data/SampleCSVFile_11kb.csv 11.0 kB pandas_csv

    Python 2.7.10 (default, May 26 2015, 13:01:57)
    Type "copyright", "credits" or "license" for more information.

    IPython 4.0.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.
    1 files loaded:

    f1 test/data/SampleCSVFile_11kb.csv 11.0 kB pandas_csv
        pandas.DataFrame: 99 rows x 10 cols.
        Columns: 0 1 2 3 4 5 6 7 8 9

    Variables defined:
        f1 : parsed files
        loaded : object with attributes for each parsed file (abbreviated filenames, tab completes)
        loaded_filenames : dict from filename to parsed file
        loaded_absolute_filenames : dict from absolute filename to parsed file
        loaded_list : list of the parsed files

    To print this message again later, type 'info()'. To quit type 'quit()'.

    In [1]:

The variable 'f1' is a pandas DataFrame with the contents of the csv file:

::

    In [1]: f1.head()
    Out[1]:
       0                                                  1                   2  \
    0  1   Eldon Base for stackable storage shelf, platinum  Muhammed MacIntyre
    1  2  1.7 Cubic Foot Compact "Cube" Office Refrigera...        Barry French
    2  3   Cardinal Slant-D� Ring Binder, Heavy Gauge Vinyl        Barry French
    3  4                                               R380       Clay Rozendal
    4  5                           Holmes HEPA Air Purifier      Carlos Soltero

         3        4       5      6        7                               8     9
    0    3  -213.25   38.94  35.00  Nunavut          Storage & Organization  0.80
    1  293   457.81  208.16  68.02  Nunavut                      Appliances  0.58
    2  293    46.71    8.69   2.99  Nunavut  Binders and Binder Accessories  0.39
    3  483  1198.97  195.99   3.99  Nunavut    Telephones and Communication  0.58
    4  515    30.94   21.78   5.94  Nunavut                      Appliances  0.50

Additional files specified on the commandline will be in variables 'f2', 'f3', and so on.

Installation
-------------
From a git checkout:

::

    pip install .

To run the tests:

::

    nosetests
