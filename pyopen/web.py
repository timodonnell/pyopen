import requests
from six.moves import urllib

from . import temp_files

def parse_url_or_path(s):
    # urlparse will parse paths with two leading slashes (e.g. "//foo")
    # in a strange way. We collapse these paths to start with just one
    # slash.
    if s.startswith("//"):
        s = "/" + s.lstrip("/")
    return urllib.parse.urlparse(s)

def maybe_download(url_or_path):
    '''
    Return a local path to a URL or file.

    If url_or_path is a URL, download it to a temporary file and return the
    path to the temporary file. If url_or_path is a local file, just return
    it.
    '''
    parsed = parse_url_or_path(url_or_path)
    if not parsed.scheme or parsed.scheme.lower() == 'file':
        return parsed.path  # Already a local path
    return download(url_or_path)

def download(url):
    '''
    Download a url to a temporary file and return the path to it.
    '''
    temp_file = temp_files.tempfile_path(
        prefix="pyopen_",
        suffix=url.split("/")[-1])

    with open(temp_file, "wb") as fd:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        for block in response.iter_content(1048576):
            fd.write(block)
    return temp_file

