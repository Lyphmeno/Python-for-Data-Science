#!/usr/bin/env python3.10

import sys
import ft_filter


def isint(number):
    """""
    description
    :param:
    :return:
    :raises:
    """""
    try:
        int(number)
        return True
    except ValueError:
        return False


def isalphasp(str):
    """""
    description
    :param:
    :return:
    :raises:
    """""
    return all(c.isalpha() or c.isspace() for c in str)


def main():
    """""
    description
    :param:
    :return:
    :raises:
    """""
    try:
        assert len(sys.argv) == 3, "AssertionError: the arguments are bad"
        tp = type(sys.argv[1])
        assert tp == str, "AssertionError: the arguments are bad"
        assert isalphasp(sys.argv[1]), "AssertionError: the arguments are bad"
        assert isint(sys.argv[2]), "AssertionError: the arguments are bad"
        print(ft_filter.ft_filter(lambda word: len(word) > int(sys.argv[2]),
                                  sys.argv[1].split()))
    except AssertionError as err:
        print(err)
    return 0


if __name__ == '__main__':
    main()
