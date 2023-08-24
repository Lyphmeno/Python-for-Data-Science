#!/usr/bin/env python3.10

import load_image


def ft_transpose(image):
    """
    This function rotate an image as an array.

    :param: image
    :returns: Returns the transposed image
    :raises: /
    """
    h, w, channels = image.shape
    img = np.zeros((w, h, channels), dtype=np.uint8)
    for y in range(h):
        for x in range(w):
            img[x, y, :] = image[y, x, :]
    return img


def main():
    """
    This function loads an image, print its shape.
    Then transposes it and print its new shape.

    :param: /
    :returns: /
    :raises: FileNotFound, Loading the image failed
    """
    try:
        img = load_image("animal.jpeg")
        if img == None:
            raise ("Loading the image failed")
        h, w, channels = img.shape
        imgarr = np.array(img)
        size = h if h < w else w
        square_part = imgarr[start_y:start_y+size, start_x:start_x+size, :]
        print("New shape after slicing:", np.array(img).shape)
        newimg.show()
    except Exception as e:
        print(f"{e}")

if __name__ == "__main__":
    main()


"NOT FINISHED AT ALL BUT ITS BORING"