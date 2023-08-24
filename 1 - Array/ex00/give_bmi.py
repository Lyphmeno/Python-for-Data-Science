#!/usr/bin/env python3.10

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI (Body Mass Index) for a list of individuals.

    Args:
        height (list[int | float]): A list of heights
        weight (list[int | float]): A list of weights

    Returns:
        Returns list[int | float]: A list of calculated BMI values.
        Returns an empty list if there are errors in input data.

    Raises:
        ValueError: If the lengths of the 'height' and 'weight' lists are not the same,
                    or if any height or weight is not a valid integer or float,
                    or if weight is not a positive value.
    """
    try:
        if len(height) != len(weight):
            raise(ValueError("'height' and 'weight' lists must be the same."))
        if not all(isinstance(height, int) for i in height):
            raise(ValueError("'height' elements must be int of float"))
        if not all(isinstance(weight, int) for i in weight):
            raise(ValueError("'weight' elements must be int of float"))
        bmi = []
        for h, w in zip(height, weight):
            if w <= 0:
                rais(ValueError)
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
    res = []
    for i in bmi:
        if i > limit:
            res.append(True)
        else:
            res.append(False)
    return res
