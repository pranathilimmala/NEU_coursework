

"""
File: test_io_utils.py
Program for running the unit tests
"""

import pytest
from assignment4.io_utils import get_fh

# pylint: disable=C0103

TEST_FILE = "C:\\users\\Lenovo\\PycharmProjects\\pythonProject" \
    "\\pranathi_limmala\\Programming_6200\\assignment_04\\chr21_genes.txt"

FILE_lINES = """
TPTE  tensin, putative protein-tyrosine phosphatase, EC 3.1.3.48. 1.1
CYC1LP4  cytochrome c pseudogene  5
Pseudo1  putative zinc finger protein pseudogene  5
PRED1  putative gene, protein kinase C ETA type (EC 2.7.1.) like 3.2
ORLP1  pheromone receptor pseudogene  5
"""


def test_get_fh_reading():
    """Function to test for reading in get file handle function"""
    test = get_fh(TEST_FILE, "r")
    assert hasattr(test, "readline") is True, "Not able to open for reading"


def test_get_fh_writing():
    """Function to test for writing in get file handle function"""
    test = get_fh('test.txt', "w")
    assert hasattr(test, "write") is True, "Not able to open for writing"


def test_get_fh_IOError():
    """Function to test IO error"""
    with pytest.raises(IOError):
        get_fh("does_not_exist.txt", "r")


def test_get_fh_ValueError():
    """Function to test Value error"""
    with pytest.raises(ValueError):
        get_fh("does_not_exist.txt", "rrr")


if __name__ == '__main__':
    test_get_fh_reading()
    test_get_fh_writing()
    test_get_fh_IOError()
    test_get_fh_ValueError()
