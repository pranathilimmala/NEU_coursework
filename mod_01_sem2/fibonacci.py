#!/usr/bin/env bash

import sys

"""Problem 6: 
    fibonacci.py"""

# This program prints the population size
# at the given day.


def population(n, k):
    """function:
    population"""
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + (dp[i-2] * k)
        return dp[n]

if __name__ == "__main__":
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    print(population(n, k))

