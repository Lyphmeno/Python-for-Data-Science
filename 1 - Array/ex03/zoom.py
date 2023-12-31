#!/usr/bin/env python3.10

from load_image import ft_load
from PIL import Image


def main():
    """
    Load an image, zoom on it, and display the new shape and image.

    Returns:
        None

    Raises:
        FileNotFoundError: If the image loading fails.
    """
    try:
        img = ft_load("animal.jpeg")
        if img is None:
            raise FileNotFoundError("Loading the image failed")
        newimg = img[100:500, 450:850, 0]
        print("New shape after slicing:", newimg.shape, "\n", newimg)
        Image.fromarray(newimg).show()
    except FileNotFoundError as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
