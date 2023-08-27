#!/usr/bin/env python3.10

def square(x: int | float) -> int | float:
    """
    Calculate the square of a given number.

    Args:
        x (int | float): The input number.

    Returns:
        int | float: The square of the input number.
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Calculate the power of a number to itself.

    Args:
        x (int | float): The input number.

    Returns:
        int | float: The result of raising the number to itself.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Create a function that applies the given function to the input number

    Args:
        x (int | float): The input number.
        function (callable): The function to apply.

    Returns:
        function: that applies the given function to x, increasing each time.
    """
    count = [0]

    def inner() -> float:
        """
        Inner function that applies the given function to x

        Returns:
            float: The result of applying the function to x.
        """
        count[0] += 1
        return function(x) ** count[0]
    return inner
