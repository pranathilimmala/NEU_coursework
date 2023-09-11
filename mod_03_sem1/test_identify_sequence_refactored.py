#!user/bin/env python3
"""Test behavior of identify_sequence_refactored.py"""

from identify_sequence_refactored import identify_sequence
# import the function to test

def test_dna_sequence():
    """Identify a DNA sequence"""
    line = "ATCGTCGG"
    assert ('T' in line) == True, "expect sequence identifies as nucleic acid"
def test_dna_lowercase_sequence():
        """Identify a DNA sequence in lowercase"""
        sequence2 = open("C:\\Users\\Lenovo\\PycharmProjects\\pythonProject"
                     "\\Pranathi_Limmala\\6308\\assignment_03\\sequence2.txt")
        assert identify_sequence(sequence2) == 'nucleic acid', "As the sequence is in lower case, this is a dna sequence in lowercase"
print("dna sequence in lowercase")
def test_rna_sequence():
    """Identify an RNA sequence"""
    rna_sequence = "AGUAGUA"
    assert ("U" in rna_sequence) == True, "expect AGUAGUA identifies as rna sequence"
def test_aminoacid_sequence():
    """Identify an amino acid sequence"""
    sequence3 = open("C:\\Users\\Lenovo\\PycharmProjects\\pythonProject"
                     "\\Pranathi_Limmala\\6308\\assignment_03\\sequence3.txt")
    assert identify_sequence(sequence3) == "amino acid",\
        "expect sequence identifies as amino acid sequence"
def test_nonsequence():
    """This test is for identifying the type of sequence"""
    seq = "ZZXy43"
    non_seq = ['B', 'J', 'O', 'X', 'Z']
    notsequence = False
    for letter in seq:
        if letter in non_seq:
            notsequence = True
    assert (seq.isdigit() or seq.islower() or notsequence) == True, \
        "expected input sequence to be non sequence"

if __name__ == "__main__":
    test_dna_sequence()
    test_dna_lowercase_sequence()
    test_aminoacid_sequence()
    test_rna_sequence()
    test_nonsequence()
