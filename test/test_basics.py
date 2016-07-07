from nose.tools import eq_
from . import data_path, run_and_capture

def test_csv():
    eq_(
        run_and_capture(
            "print(f1.shape)",
            [data_path("SampleCSVFile_11kb.csv")]),
        "(99, 10)")
    eq_(
        run_and_capture(
            "print(f1.shape)",
            [data_path("SampleCSVFile_11kb.csv.gz")]),
        "(99, 10)")
    eq_(
        run_and_capture(
            "print(f1.shape)",
            [data_path("SampleCSVFile_11kb.csv.bz2")]),
        "(99, 10)")
    eq_(
        run_and_capture(
            "print(f1.shape)",
            [
                data_path("SampleCSVFile_11kb.csv.nonstandard_extension"),
                "--loader", "pandas_csv",
            ]),
        "(99, 10)")

def test_tsv():
    eq_(
        run_and_capture(
            "print(f1.shape)",
            [
                data_path("nasa_19950801.tsv.bz2"),
                "--loader", "pandas_csv",
            ]),
        "(30969, 9)")

def test_xls():
    eq_(
        run_and_capture(
            "print(f1['Sample-spreadsheet-file'].shape)",
            [data_path("SampleXLSFile_38kb.xls")]),
        "(99, 10)")

def test_json():
    eq_(
        run_and_capture(
            "print(f1['glossary']['title'])",
            [data_path("example1.json")]),
        "example glossary")

def test_pickle():
    eq_(
        run_and_capture(
            "print(f1['glossary']['title'])",
            [data_path("example1.pkl")]),
        "example glossary")