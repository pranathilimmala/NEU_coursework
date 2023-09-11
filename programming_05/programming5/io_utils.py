

"""
File: io_utils.py
"""
import sys
import os


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

def is_gene_file_valid(file):
    """
    check if input file exits
    :param file: file
    :return: True/False
    """
    if os.path.exists(file):
        return True
    else:
        return False
