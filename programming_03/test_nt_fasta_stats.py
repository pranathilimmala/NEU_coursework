"""test_nt_fasta_stats.py"""

import pytest
from nt_fasta_stats import get_filehandle, _get_num_nucleotides, _get_ncbi_accession, _verify_lists


def test_get_filehandle():
    with pytest.raises(OSError):
        get_filehandle("does_not_exist.txt", "r")

    with pytest.raises(ValueError):
        get_filehandle("influenza.fasta", "rrr")


def test_get_num_nucleotides():
    seq = 'AACAGCACGGCAACGCTGTGCCTTGGGCACCATGCAGTACCAAACGGAACGATAG' \
          'TGAAAACAATCACGAATGACCAAATTGAAGTTACTAATGCTACTGAGCT' \
          'GGTTCAGAGTTCCTCAACAGGTGAAATATGCGACAGTCCTCATCAGATCCTTGATGGA' \
          'GAAAACTGCACACTAATAGATGCTCTATTGGGAGACCCTCAGTGTGA' \
          'TGGCTTCCAAAATAAGAAATGGGACCTTTTTGTTGAACGCAGCAAAGCCTACAGCAACTGTTACCCTT' \
          'ATGATGTGCCGGATTATGCCTCCCTTAGGTCACTAGTTGCCTCATCCGGCACACTGGAATTTAACAATGA' \
          'AAGCTTCAATTGGACTGGAGTCACTCAAAATGGAACAAGCTCTG' \
          'CTTGCAAAAGGAGATCTAATAACAGTTT' \
          'CTTTAGTAGATTGAATTGGTTGACCCACTTAAAATTCAAATACCCAGCATTGAACGTGACTATGCCAAAC' \
          'AATGAAAAATTTGACAAATTGTACATTTGGGGGGTTCACCACCCGGGTACGGACAATGACCAAATCTTC' \
          'CTGTATGCTCAAGCATCAGGAAGAATCACAGTCTCTACCAAAAGAAGC' \
          'CAACAGACTGTAATCCCGAATATC' \
          'GGATCTAGACCCAGAGTAAGGAATATCCCCAGCAGAATAAGCATCTATTGGACAATAGTAAAACCGGGAG' \
          'ACATACTTTTGATTAACAGCACAGGGAATTTAATTGCTCCTAGGGGTTACTTCAAAATACGAAGTGGGAAAAGC' \
          'TCAATAATGAGATCAGATGCACCCATTGGCAAATGCAATTCTGAATGCATCACTCCAAATGGAAGCATTCCCAATG' \
          'ACAAACCATTTCAAAATGTAAACAGGATCACATATGGGGCCTGTCCCAGATATGTTAAGCAAAACACTCTGAAATT' \
          'GGCAACAGGGATGCGAAATGTACCAGAGAAACAAACTAGAGGCATATTTGGCGCAATCGCGGGT' \
          'TTCATAGAAAATGGTTGGGAAGGAATGGTGGATGGTTGGTACGGTTT'

    with pytest.raises(SystemExit):
        _get_num_nucleotides('Y', seq)
    assert _get_num_nucleotides('A', seq) == 350
    assert _get_num_nucleotides('G', seq) == 225
    assert _get_num_nucleotides('C', seq) == 217
    assert _get_num_nucleotides('T', seq) == 245
    assert _get_num_nucleotides('N', seq) == 0


def test_get_ncbi_accession():
    header = '>EU521893 A/Arequipa/FLU3833/2006 2006// 4 (HA)'
    assert _get_ncbi_accession(header) == '>EU521893'


def test_verify_lists():
    header_list = ['>EU521893 A/Arequipa/FLU3833/2006 2006// 4 (HA)']
    seq_list = []
    with pytest.raises(SystemExit):
        _verify_lists(header_list, seq_list)

if __name__ == '__main__':
    test_get_filehandle()
    test_get_num_nucleotides()
    test_get_ncbi_accession()
    test_verify_lists()
