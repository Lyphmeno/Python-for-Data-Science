#!/usr/bin/env python3.10

from PIL import Image
from load_image import ft_load
import numpy as np


def main():
    """
    Loads an image, cuts a square part from it, transposes it.
    Displays the new shape and result.

    Returns:
        None

    Raises:
        FileNotFoundError: If the image loading fails.
    """
    try:
        img = ft_load("animal.jpeg")
        if img is None:
            raise FileNotFoundError("Loading the image failed")
        newimg = img[100:500, 450:850]
        newimg = np.array(list(zip(*newimg)))
        print("New shape after slicing:", newimg.shape, "\n", newimg)
        Image.fromarray(newimg).show()
    except FileNotFoundError as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
