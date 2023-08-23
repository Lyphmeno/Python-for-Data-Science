#!/usr/bin/env python3.10

import sys


def main():
    """main of the program, nothing much to say here..."""
    punc = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    if len(sys.argv) < 2:
        return 1
    try:
        assert len(sys.argv) == 2, \
            "AssertionError: more than one argument is provided"
        print(f"What is the text to count?")
        print(f"{sys.argv[1]}")
        print(f"The text contains {len(sys.argv[1])}")
        print(sum(1 for c in sys.argv[1] if c.isupper()), "upper letters")
        print(sum(1 for c in sys.argv[1] if c.islower()), "lower letters")
        print(sum(1 for c in sys.argv[1] if c in punc), "ponctuation mark")
        print(sum(1 for c in sys.argv[1] if c.isspace()), "space")
        print(sum(1 for c in sys.argv[1] if c.isdigit()), "digits")
    except AssertionError as err:
        print(err)


if __name__ == "__main__":
    main()
