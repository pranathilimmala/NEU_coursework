#!/usr/bin/env bash

import sys

"""Problem 5: 
    hamming.py"""

# This program helps us find the hamming distance
# which is one of several string metrics for measuring
# the edit distance between two sequences.


def hamming(str1, str2):
    """function:
    hamming"""
    h_distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            h_distance += 1
    return h_distance

if __name__ == "__main__":
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    distance = hamming(str1, str2)
    print(f"{str1}\t{str2}\t{distance}")
