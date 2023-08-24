#!/user/bin/env python3.10

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Print the shape of an array.
    Returns a truncated version of a 2D array based on start and end indices.
    Print the new shape of an array.

    Args:
        family (list): 2D array of numbers.
        start (int): Start index of the slicing.
        end (int): End index of the slicing.

    Returns:
        list: A truncated version of the array based on start/end indices.

    Raises:
        ValueError: If values in the array are neither int nor float.
    """
    try:
        if not all(isinstance(height, int | float) for i in family):
            raise(ValueError("Array elements must be int or float"))
        print("My shape is : ", np.array(family).shape)
        res = [row for row in family[start:end]]
        print("My shape is : ", np.array(res).shape)
        return res
    except Exception as e:
        print(f"{e}")
        return []
