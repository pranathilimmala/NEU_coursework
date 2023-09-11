#!/usr/bin/env bash

"""Problem 1:
    Basic functions"""

# This program helps us to understand the basic functions
# involved in solving different things using Python


def multiply(a, b):
    return a * b

def hello_name(name="you"):
    return f"Hello, {name}!"

def less_than_ten(numbers):
    return [n for n in numbers if n < 10]
