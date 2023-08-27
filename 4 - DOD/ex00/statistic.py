#!/usr/bin/env python3.10

def stat(*args: any, **kwargs: any) -> None:
    """
    Calculate statistical measures for a list of numerical values.

    Args:
        *args: Variable-length argument list containing numerical values.
        **kwargs: arguments specifying the statistical measures to calculate.
            Supported kwargs:
                - 'mean': mean (average) of the values.
                - 'median': median (middle value) of the values.
                - 'quartile': 25th and 75th quartiles of the values.
                - 'std': standard deviation of the values.
                - 'var': variance of the values.

    Returns:
        None: Prints the calculated statistical measures for the given values.
    """
    for val in kwargs.values():
        larg = len(args)
        if larg == 0:
            print("ERROR")
            continue
        sarg = sorted(args)
        if val == "mean":
            res = sum(sarg) / larg
        elif val == "median":
            res = sarg[larg // 2] if larg % 2 == 0 else sarg[larg // 2 + 1]
        elif val == "quartile":
            q25 = sarg[int(0.25 * larg)]
            q75 = sarg[int(0.75 * larg)]
            res = q25, q75
        elif val == "std":
            mean = sum(sarg) / larg
            squared_diff = [(x - mean) ** 2 for x in sarg]
            variance = sum(squared_diff) / (larg - 1)
            res = variance ** 0.5
        elif val == "var":
            mean = sum(sarg) / larg
            squared_diff = [(x - mean) ** 2 for x in sarg]
            res = sum(squared_diff) / (larg - 1)
        print(res)
