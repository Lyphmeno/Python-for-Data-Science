#!/usr/bin/env python3.10


def square(x: int | float) -> int | float:
    """
    Calculate the square of a given number.

    Args:
        x (int | float): The input number.

    Returns:
        int | float: The square of the input number.
    """
    try:
        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError("x must be an int or a float.")
        return x * x
    except Exception as msg:
        print(msg)


def pow(x: int | float) -> int | float:
    """
    Calculate the power of a number to itself.

    Args:
        x (int | float): The input number.

    Returns:
        int | float: The result of raising the number to itself.
    """
    try:
        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError("x must be an int or a float.")
        return x ** x
    except Exception as msg:
        print(msg)


def outer(x: int | float, function) -> object:
    """
    Create a function that applies the given function to the input number

    Args:
        x (int | float): The input number.
        function (callable): The function to apply.

    Returns:
        function: that applies the given function to x, increasing each time.
    """
    try:
        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError("x must be an int or a float.")
        count = 0
        result = None

        def inner() -> float:
            """Apply function on x"""
            nonlocal count, result
            if count == 0:
                result = x
            result = function(result)
            count += 1
            return result
        return inner
    except Exception as msg:
        print(msg)
