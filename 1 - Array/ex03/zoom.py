#!/usr/bin/env python3.10

import load_image
import numpy as np


def main():
    """
    Load an image, zoom on it, and display the new shape and image.

    Returns:
        None

    Raises:
        FileNotFoundError: If the image loading fails.
    """
    try:
        img = load_image("animal.jpeg")
        if img is None:
            raise FileNotFoundError("Loading the image failed")
        newimg = img.resize((img.size[0] * 2, img.size[1] * 2))
        print("New shape after slicing:", np.array(newimg).shape)
        newimg.show()
    except FileNotFoundError as e:  # Catch the specific exception
        print(f"{e}")


if __name__ == "__main__":
    main()
