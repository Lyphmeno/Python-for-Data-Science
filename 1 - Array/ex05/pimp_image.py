#!/usr/bin/env python3.10

import numpy as np


def ft_invert(array) -> np.array:
    """
    This function invert the color of an image by changing the rgb channel.

    :param array: array image
    :returns: Returns the modified array
    :raises: /
    """
    return np.mqx(array) - array


def ft_red(array) -> np.array:
    """
    This function apply a red filter on an image by changing the rgb channel.

    :param array: array image
    :returns: Returns the modified array
    :raises: /
    """
    array[:, :, 0] = 255
    return array


def ft_green(array) -> np.array:
    """
    This function apply a red filter on an image by changing the rgb channel.

    :param array: array image
    :returns: Returns the modified array
    :raises: /
    """
    array[:, :, 1] = 255
    return array


def ft_blue(array) -> np.array:
    """
    This function apply a blue filter on an image by changing the rgb channel.

    :param array: array image
    :returns: Returns the modified array
    :raises: /
    """
    array[:, :, 2] = 255
    return array


def ft_grey(array) -> np.array:
    """
    This function apply a grey filter on an image by changing the rgb channel.

    :param array: array image
    :returns: Returns the modified array
    :raises: /
    """
    val = np.mean(array, axis=2, dtype=int)
    newarr = np.zeros_like(array)
    for i in range(3):
        newarr[:, :, i] = val
    return newarr
