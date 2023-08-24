#!/usr/bin/env python3.10


def ft_filter(func, iter):
    """""
    description
    :param:
    :return:
    :raises:
    """""
    new = [x for x in iter if func(x) is True]
    return new
