#!/usr/bin/env python3.10

from PIL import Image
import numpy as np

def ft_load(path: str) -> array:
    try:
        img = Image.open(path)
        print("The shape of the image is:", np.array(img).shape)
        print(np.array(img))
        return img
    except FileNotFoundError as e:
        print(f"{e}")
        return None

