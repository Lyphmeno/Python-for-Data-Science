#!/usr/bin/env python3.10

import sys


def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def odd_or_even():
    if len(sys.argv) < 2:
        return 1
    try:
        assert len(sys.argv) == 2, \
            "AssertionError: more than one argument is provided"
        assert is_int(sys.argv[1]), \
            "Assertion error: argument is  not an integer"
        if int(sys.argv[1]) % 2 != 0:
            print("I'm Odd.")
        else:
            print("I'm Even.")
    except AssertionError as error:
        if error != "":
            print(error)


odd_or_even()
