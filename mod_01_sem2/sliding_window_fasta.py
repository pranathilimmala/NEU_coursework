#!/usr/bin/env bash

import sys
from sliding_window import sliding_window, gc_content


"""Problem 4: 
    sliding_window_fasta.py"""

# This program uses sliding_window function and thereby gives us
# kmer strings and gc content of the fasta input file

if __name__ == "__main__":
    k = int(sys.argv[1])
    fasta_file = sys.argv[2]
    current_header = ""
    with open(fasta_file, 'r') as f:
        for line in f:
            if line[0] == ">":
                current_header = line.strip()
                print(current_header)
            else:
                sequence = line.strip()
                kmers = sliding_window(k, sequence)
                for kmer in kmers:
                    gc = gc_content(kmer)
                    print(f"{kmer}\t{format(gc,'.2f')}")
