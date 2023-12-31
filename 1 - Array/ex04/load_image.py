#!/usr/bin/env python3.10

from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Load an image using PIL.

    Args:
        path (str): Path of the image.

    Returns:
        np.array: The loaded image as a NumPy array.

    Raises:
        FileNotFoundError: If the specified path is incorrect.
    """
    try:
        img = np.array(Image.open(path))
        print("The shape of the image is:", img.shape)
        print(img)
        return img
    except FileNotFoundError as e:
        print(f"{e}")
        return None
    except AttributeError:
        print("Error : empty file path")
        return None
