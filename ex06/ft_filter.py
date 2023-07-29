#!/usr/bin/env python3.10


def ft_filter(func, iter):
    """The ft_filter() function selects elements from an iterable \
(list, tuple etc.) based on the output of a function.\
The function is applied to each element of the iterable and if it returns \
True, the element is selected by the ft_filter() function."""
    new = [x for x in iter if func(x) is True]
    return new
