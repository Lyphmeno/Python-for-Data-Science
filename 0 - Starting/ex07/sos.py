#!/usr/bin/env python3.10

import sys


def main():
    """
    Encodes a string in morse code and display it in the ternimal.

    Args:
        sys.argv[1] (str): the string to encode.

    Returns: /

    Raises:
        Assertion Error: when a character is not alphanumerical or space.
    """
    try:
        NESTED_MORSE = {
            " ": "/",
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "0": "-----",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
        }
        assert len(sys.argv) == 2, "AssertionError: the arguments are bad"
        assert all(c.isalnum() or c.isspace() for c in sys.argv[1]), \
            "AssertionError: the arguments are bad"
        print(*(NESTED_MORSE.get(c.upper()) for c in sys.argv[1]))
    except Exception as msg:
        print(msg)


if __name__ == "__main__":
    main()