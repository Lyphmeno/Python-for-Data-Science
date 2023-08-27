#!/usr/bin/env python3.10

from PIL import Image
from load_image import ft_load


def ft_transpose(image):
    """
    Rotate an image (array) by transposing its dimensions.

    Args:
        image: The input image as array.

    Returns:
        img_transposed: The transposed image/array.

    Raises:
        None
    """
    h, w, channels = image.shape
    img_transposed = image.transpose(1, 0, 2)
    return img_transposed


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
        h, w, channels = img.shape
        size = min(h, w)
        start_x = 0
        start_y = 0
        square_arr = img[start_y:start_y + size, start_x:start_x + size, :]
        newarr = ft_transpose(square_arr)
        print("The shape of the image is:", img.shape)
        print("New shape after Transpose:", newarr.shape)
        newimg = Image.fromarray(newarr)
        newimg.show()
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
