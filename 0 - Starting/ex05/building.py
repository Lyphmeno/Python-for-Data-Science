#!/usr/bin/env python3.10

import sys


def main():
    """main of the program, nothing much to say here..."""
    punc = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    try:
        assert len(sys.argv) <= 2, \
            "AssertionError: more than one argument is provided"
        if len(sys.argv) > 1:
            str = sys.argv[1]
        else:
            str = input("What is the text to count?\n")
        print(f"The text contains {len(str)} characters:")
        print(sum(1 for c in str if c.isupper()), "upper letters")
        print(sum(1 for c in str if c.islower()), "lower letters")
        print(sum(1 for c in str if c in punc), "ponctuation mark")
        print(sum(1 for c in str if c.isspace()), "spaces")
        print(sum(1 for c in str if c.isdigit()), "digits")
    except AssertionError as err:
        print(err)


if __name__ == "__main__":
    main()
