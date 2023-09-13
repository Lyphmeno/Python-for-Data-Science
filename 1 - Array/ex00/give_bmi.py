#!/usr/bin/env python3.10


def give_bmi(height: list[int | float], weight: list[int | float]) ->\
        list[int | float]:
    """
    Calculate BMI (Body Mass Index) for a list of individuals.

    Args:
        height (list[int | float]): A list of heights
        weight (list[int | float]): A list of weights

    Returns:
        list[int | float]: A list of calculated BMI values.
        empty list if there are errors in input data.

    Raises:
        ValueError: If the len of 'height' and 'weight' lists are not the same.
                    If 'height' or 'weight' is not a valid integer or float.
                    If 'weight' is not a positive value.
    """
    try:
        if len(height) != len(weight):
            raise ValueError("'height' and 'weight' lists must be the same.")
        if not all(isinstance(i, int | float) for i in height):
            raise TypeError("'height' elements must be int of float")
        if not all(isinstance(i, int | float) for i in weight):
            raise TypeError("'weight' elements must be int of float")
        bmi = []
        for h, w in zip(height, weight):
            if w <= 0:
                raise (ValueError)
            val = w / (h ** 2)
            bmi.append(val)
        return bmi
    except Exception as e:
        print(f"{e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    This function check if every bmi of the list if above a limit.

    :param list[int | float]: bmi list
    :param int: limit
    :returns: Returns a list[bool] (True if above the limit)
    :raises: /
    """
    if not all(isinstance(i, int | float) for i in bmi):
        raise TypeError("'bmi' elements must be int of float")
    if not isinstance(limit, int):
        raise TypeError("limit must be int of float")
    res = []
    for i in bmi:
        if i > limit:
            res.append(True)
        else:
            res.append(False)
    return res


height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
