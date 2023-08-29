#!/usr/bin/env python3.10


def ft_tqdm(lst: range) -> None:
    """
    Print a dynamic progress bar based on the iteration over a range.

    Args:
        lst (range): The range object over which the iteration is performed.

    Yields:
        int: The current iteration value from the range.

    Raise: /

    Example:
        for i in ft_tqdm(range(100)):
            time.sleep(0.1)
    """
    lstlen = len(lst)
    lst = range(len(lst) + 1)
    for i in lst:
        num = int(204 * i / lstlen)
        bar = "█" * num + " " * (204 - num)
        percentage = round(i / lstlen * 100)
        print(f"\r{percentage}%|{bar}| {i}/{lstlen}", end="")
        yield i
