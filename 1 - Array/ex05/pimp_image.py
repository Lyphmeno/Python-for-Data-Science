#!/usr/bin/env python3.10

import numpy as np


def ft_invert(array) -> np.array:
    """Inverts the color of the image received."""
    return 255 - array


def ft_red(array) -> np.array:
    """Apply a red filter on an image by changing the rgb channel."""
    newarr = array.copy()
    newarr[:, :, 1] = 0
    newarr[:, :, 2] = 0
    return newarr


def ft_green(array) -> np.array:
    """Apply a green filter on an image by changing the rgb channel."""
    newarr = array.copy()
    newarr[:, :, 0] = 0
    newarr[:, :, 2] = 0
    return newarr


def ft_blue(array) -> np.array:
    """Apply a blue filter on an image by changing the rgb channel."""
    newarr = array.copy()
    newarr[:, :, 0] = 0
    newarr[:, :, 1] = 0
    return newarr


def ft_grey(array) -> np.array:
    """Apply a grey filter on an image by changing the rgb channel."""
    val = np.mean(array, axis=2, dtype=int)
    newarr = np.zeros_like(array)
    for i in range(3):
        newarr[:, :, i] = val
    return newarr
