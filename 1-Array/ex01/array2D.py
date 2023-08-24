#!/user/bin/env python3.10

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    This function print the shape of a 2D array.

    :param list: 2D array of numbers
    :param int: start of the slicing
    :param int: end of the slicing
    :returns: Returns a truncated version of the array based on start/end
    :raises: ValueError if values in array are neither int or float
    """
    try:
        if not all(isinstance(height, int | float) for i in family):
            raise(ValueError)
        print("My shape is : ", np.array(family).shape)
        res = [row for row in family[start:end]]
        print("My shape is : ", np.array(res).shape)
        return res
    except Exception as e:
        print(f"{e}")
        return []
