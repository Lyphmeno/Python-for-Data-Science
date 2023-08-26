#!/usr/bin/env python3.10


def ft_filter(func, iter):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    new = [x for x in iter if func(x) is True]
    return new
