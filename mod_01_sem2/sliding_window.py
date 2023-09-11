#!/usr/bin/env bash

import sys


"""Problem:3
sliding_window.py"""

# This program helps us to understand and derive kmer strings
# and gc content for the sequence


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

if __name__ == "__main__":
    k = int(sys.argv[1])
    string = sys.argv[2]
    kmers = sliding_window(k, string)
    for kmer in kmers:
        gc = gc_content(kmer)
        print(f"{kmer}\t{round(gc, 2)}")
