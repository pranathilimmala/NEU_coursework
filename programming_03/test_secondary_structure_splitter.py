'''test_secondary_structure_splitter'''

import pytest
from secondary_structure_splitter import get_filehandle, _verify_lists


def test_get_filehandle():
    with pytest.raises(OSError):
        get_filehandle("does_not_exist.txt", "r")

    with pytest.raises(ValueError):
        get_filehandle("influenza.fasta", "rrrrrr")

def test_verify_lists():
    list_headers = ['>EU521893 A/Arequipa/FLU3833/2006 2006// 4 (HA)']
    list_seq = []
    with pytest.raises(SystemExit):
        _verify_lists(list_headers, list_seq)

if __name__ == '__main__':
    test_get_filehandle()
    test_verify_lists()
