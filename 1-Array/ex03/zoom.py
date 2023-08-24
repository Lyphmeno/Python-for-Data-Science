#!/usr/bin/env python3.10

import load_image

def main():
    """
    This function print the shape of the image.
    Zoom on the image given and print the new shape.

    :param: / 
    :returns: Returns the sliced image
    :raises: FileNotFound, Loading the image failed
    """
    try:
        img = load_image("animal.jpeg")
        if img == None:
            raise ("Loading the image failed")
        newimg = img.resize(img.siwe[0] * 2, img.size[1] * 2)
        print("New shape after slicing:", np.array(img).shape)
        newimg.show()
    except Exception as e:
        print(f"{e}")

if __name__ == "__main__":
    main()
