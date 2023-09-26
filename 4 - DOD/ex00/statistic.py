#!/usr/bin/env python3.10


def ft_statistics(*args: any, **kwargs: any) -> None:
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
    try:
        for val in kwargs.values():
            larg = len(args)
            if larg == 0:
                print("ERROR")
                continue
            sarg = sorted(args)
            if val == "mean":
                res = sum(sarg) / larg
                print(f"mean : {res}")
            elif val == "median":
                res = sarg[larg // 2] if larg % 2 == 1 else sarg[larg // 2 + 1]
                print(f"median : {res}")
            elif val == "quartile":
                q25 = sarg[int(0.25 * larg)]
                q75 = sarg[int(0.75 * larg)]
                res = [float(q25), float(q75)]
                print(f"quartile : {res}")
            elif val == "std":
                mean = sum(sarg) / larg
                var = sum(pow(x - mean, 2) for x in args) / larg
                res = var ** 0.5
                print(f"std : {res}")
            elif val == "var":
                mean = sum(sarg) / larg
                res = sum(pow(x - mean, 2) for x in args) / larg
                print(f"var : {res}")
    except Exception as e:
        print(f"ERROR: {e}")
