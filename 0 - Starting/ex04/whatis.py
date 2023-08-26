#!/usr/bin/env python3.10

import sys


def is_int(number):
    """
    Check if value is type of int.

    Args:
        number any: Value to check

    Returns:
        Returns True if int False if not.

    Raises: /
    """
    try:
        int(number)
        return True
    except ValueError:
        return False


def odd_or_even():
    """
    Check if value is odd or even and print the result.

    Args:
        sys.argv[1]: Value to check.

    Returns: /

    Raises:
        AssertionError: If len(arg) != 2
        AssertionError: if value isnt an int
    """
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
    except Exception as error:
        if error != "":
            print(error)


odd_or_even()
