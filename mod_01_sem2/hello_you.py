#!/usr/bin/env bash

import sys

"""Problem 2: 
    hello_you.py"""

# This function returns the name,
# so it lets us know the basic functions
# used in python programming

def hello_name(name="you"):
    """function:
    hello_name"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "you"
    print(hello_name(name))
