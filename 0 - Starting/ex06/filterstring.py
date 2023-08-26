#!/usr/bin/env python3.10

import sys
import ft_filter


def isint(number):
    """
    Check if a given value is a valid integer.

    Args:
        number: The value to be checked.

    Returns:
        bool: True if the value can be converted to an integer.
              False otherwise.

    Raise: /
    """
    try:
        int(number)
        return True
    except ValueError:
        return False


def isalnumsp(str):
    """
    Check if a given text contains only alphabetical characters or spaces.

    Args:
        text (str): The text to be checked.

    Returns:
        bool: True if the text contains only alphabetical characters or spaces.
              False otherwise.

    Raise: /
    """
    return all(c.isalnum() or c.isspace() for c in str)


def main():
    """
    Check if a given text contains only alphabetical characters or spaces.

    Args:
        text (str): The text to be checked.

    Returns:
        bool: True if the text contains only alphabetical characters or spaces.
              False otherwise.

    Raise: /
    """
    try:
        assert len(sys.argv) == 3, "AssertionError: the arguments are bad"
        tp = type(sys.argv[1])
        assert tp == str, "AssertionError: the arguments are bad"
        assert isalnumsp(sys.argv[1]), "AssertionError: the arguments are bad"
        assert isint(sys.argv[2]), "AssertionError: the arguments are bad"
        print(ft_filter.ft_filter(lambda word: len(word) > int(sys.argv[2]),
                                  sys.argv[1].split()))
    except AssertionError as err:
        print(err)
    return 0


if __name__ == '__main__':
    main()
