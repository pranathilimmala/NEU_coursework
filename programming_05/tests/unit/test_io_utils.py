
"""Test for module io_utils.py"""
import os
import pytest
from assignment5 import io_utils

#ignore all "Missing function or method docstring" since this is a unit test.
#ignore all "Function name "test_get_fh_4_IOError" doesn't conform to snake_case naming style"
#ignore all "Function name "test_get_fh_4_OSError" doesn't conform to snake_case naming style"
#ignore all "Function name "get_error_string_4_ValueError" doesn't conform to snake_case naming style"
#ignore all "Function name "get_error_string_4_TypeError" doesn't conform to snake_case naming style"
# pylint: disable=C0116


FILE_2_TEST = "file.txt"

def _create_test_file(file):
    """_create_test_file"""

    open(file, "w").close()


def test_is_gene_file_valid():
    """test_is_gene_file_valid"""

    _create_test_file(FILE_2_TEST)
    assert io_utils.is_gene_file_valid(FILE_2_TEST) == True, "Not valid file"
    os.remove(FILE_2_TEST)


def test_existing_get_fh_4_reading():
    """test_existing_get_fh_4_reading"""
    _create_test_file(FILE_2_TEST)
    test = io_utils.get_fh(FILE_2_TEST, "r")
    assert hasattr(test, "readline") == True, "Not able to open for reading"
    test.close()
    os.remove(FILE_2_TEST)


def test_existing_get_fh_4_writing():
    """test_existing_get_fh_4_writing"""

    test = io_utils.get_fh(FILE_2_TEST, "w")
    assert hasattr(test, "write") == True, "Not able to open for writing"
    test.close()
    os.remove(FILE_2_TEST)


def test_get_fh_4_ValueError():
    """test_get_fh_4_ValueError"""

    _create_test_file(FILE_2_TEST)
    with pytest.raises(ValueError):
        io_utils.get_fh("test.txt", "rrr")
        os.remove(FILE_2_TEST)


def test_get_fh_4_TypeError():
    """test_get_fh_4_TypeError"""

    _create_test_file(FILE_2_TEST)
    with pytest.raises(TypeError):
        io_utils.get_fh([], "r")
    os.remove(FILE_2_TEST)


def test_get_fh_4_OSError():
    """test_get_fh_4_OSError"""

    _create_test_file(FILE_2_TEST)
    with pytest.raises(OSError):
        io_utils.get_fh("does_not_exist.txt", "r")
    os.remove(FILE_2_TEST)


if __name__ == '__main__':
    test_get_fh_4_OSError()
    test_get_fh_4_TypeError()
    test_get_fh_4_ValueError()
    test_existing_get_fh_4_writing()
    test_existing_get_fh_4_reading()
    test_is_gene_file_valid()
