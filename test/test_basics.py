from nose.tools import eq_
from . import data_path, run_and_capture

RUN_TESTS_REQUIRING_INTERNET = True

SAMPLE_CSV_URL = "https://raw.githubusercontent.com/timodonnell/pyopen/master/test/data/SampleCSVFile_11kb.csv"

def test_csv():
    eq_(
        run_and_capture(
            "print(f1.shape)",
            [data_path("SampleCSVFile_11kb.csv"),
            "--csv-encoding", "latin1"]),
        "(99, 10)")
    eq_(
        run_and_capture(
            "print(f1.shape)",
            [data_path("SampleCSVFile_11kb.csv.gz"),
            "--csv-encoding", "latin1"]),
        "(99, 10)")
    eq_(
        run_and_capture(
            "print(f1.shape)",
            [data_path("SampleCSVFile_11kb.csv.bz2"),
            "--csv-encoding", "latin1"]),
        "(99, 10)")
    eq_(
        run_and_capture(
            "print(f1.shape)",
            [
                data_path("SampleCSVFile_11kb.csv.nonstandard_extension"),
                "--loader", "pandas_csv", "--csv-encoding", "latin1",
            ]),
        "(99, 10)")

if RUN_TESTS_REQUIRING_INTERNET:
    def test_csv_url():
        eq_(
            run_and_capture(
                "print(f1.shape)",
                [SAMPLE_CSV_URL, "--csv-encoding", "latin1"]),
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

def test_hdf5():
    eq_(
        run_and_capture(
            "print(f1['/detector/readout'].ix[3, 'energy'])",
            [data_path("pytables_native.h5")]),
        "6561.0")

def test_json():
    eq_(
        run_and_capture(
            "print(f1['glossary']['title'])",
            [data_path("example1.json")]),
        "example glossary")

def test_yaml():
    eq_(
        run_and_capture(
            "print(f1['glossary']['title'])",
            [data_path("example1.yaml")]),
        "example glossary")

def test_pickle():
    eq_(
        run_and_capture(
            "print(f1['glossary']['title'])",
            [data_path("example1.pkl")]),
        "example glossary")
