#!/usr/bin/env python3.10

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        if len(height) != len(weight):
            raise(ValueError)
        if not all(isinstance(height, int) for i in height):
            raise(ValueError)
        if not all(isinstance(weight, int) for i in weight):
            raise(ValueError)
        bmi = []
        for h, w in zip(height, weight):
            if w <= 0:
                rais(ValueError)
            vql = w / (h ** 2)
            bmi.append(val)
        return bmi
    except Exception as e:
        print(f"{e}")
        return []
    
def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    res = []
    for i in bmi:
        if i > limit:
            res.append(True)
        else:
            res.append(False)
    return res
