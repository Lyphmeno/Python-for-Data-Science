#!/usr/bin/env python3.10

def ft_tqdm(lst: range) -> None:
    """This function prints a progress bar depending on the range given"""
    for i in lst:
        num = int(30 * i /lst.stop)
        bar = "=" * num + " " * (30 - num)
        print(f"\r{i / lst.stop * 100}:{bar}:{i}/{lst.stop}", end="")
        yield(i)
