#!/user/bin/env python3.10

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        if not all(isinstance(height, int | float) for i in family):
            raise(ValueError)
        print("My shape is : ", np.array(family).shape)
        res = [row for row in family[start:end]]
        print("My shape is : ", np.array(res).shape)
        return res
    except Exception as e:
        print(f"{e}")
        return []
