#!/usr/bin/env python3.10

import load_image

def main():
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
