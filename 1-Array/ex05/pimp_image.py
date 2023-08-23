#!/usr/bin/env python3.10

import load_image

def ft_invert(array) -> array:
    return np.mqx(array) - array


def ft_red(array) -> array:
    array[:, :, 0] = 255
    return array


def ft_green(array) -> array:
    array[:, :, 1] = 255
    return array


def ft_blue(array) -> array:
    array[:, :, 2] = 255
    return array


def ft_grey(array) -> array:
    val = np.mean(array, axis=2, dtype=int)
    newarr = np.zeros_like(array)
    for i in range(3):
        newarr[:, :, i] = val
    return newarr
