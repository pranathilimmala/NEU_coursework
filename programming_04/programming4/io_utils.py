

"""
File: io_utils.py
"""
import sys


def get_fh(file=None, mode=None):
    """
    filehandle : get_filehandle(infile, "r")
    Takes : 2 arguments file name and mode i.e. what is needed to be done with
    this file. This function opens the file based on the mode passed in
    the argument and returns filehandle.
    """
    try:
        fobj = open(file, mode)
        return fobj
    except OSError:
        print(f"Could not open the file: {file} for type '{mode}'", file=sys.stderr)
        raise
    except ValueError:
        print(f"Could not open the file: {file} for type '{mode}'", file=sys.stderr)
        raise
