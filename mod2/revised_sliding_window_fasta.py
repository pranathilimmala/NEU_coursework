#!/usr/bin/env bash

import sys
from Bio import SeqIO

"""Problem:5
revised_sliding_window.py"""

# This program helps us to understand
# and derive kmer strings and
# gc content for the sequence


def sliding_window(k, string):
    """ function:
    sliding_window"""

    kmer_list = []
    for i in range(len(string) - k + 1):
        kmer_list.append(string[i:i+k])
    return kmer_list

def gc_content(string):
    """function:
    gc content"""
    gc_count = string.count('G') + string.count('C')
    return gc_count / len(string)

# This program uses sliding_window function and thereby gives us
# kmer strings and gc content of the fasta input file

if __name__ == "__main__":
    k = int(sys.argv[1])
    fasta_file = sys.argv[2]
    current_header = ""
    for record in SeqIO.parse(fasta_file, 'fasta'):
        sequence = str(record.seq)
        header = record.id
        kmers = sliding_window(k, sequence)
        for kmer in kmers:
            gc = gc_content(kmer)
            print(f"{header}\t{kmer}\t{format(gc,'.2f')}")
