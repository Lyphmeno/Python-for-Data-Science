#!/usr/bin/env python3.10


def callLimit(limit: int):
    """
    Create a decorator that limits the number of times a function is called.

    Args:
        limit (int): The maximum allowed number of function calls.

    Returns:
        function: A decorator that enforces the call limit on a function.
    """
    count = 0

    def callLimiter(function):
        """
        Decorator that limits the number of times a function can be called.

        Args:
            function: The function to decorate.

        Returns:
            function: The decorated function.
        """

        def limit_function(*args: any, **kwds: any):
            """
            Wrapper function that checks and enforces the call limit.

            Args:
                *args: Positional arguments for the function.
                **kwargs: Keyword arguments for the function.

            Returns:
                Any: The result of the function call if within the limit
                String: Error msg if called too much
            """
            nonlocal count
            if count >= limit:
                print(f"Error: <function {function.__name__}", end=' ')
                print(f"at {hex(id(function))}> call too many times")
            else:
                count += 1
                return function(*args, **kwds)
        return limit_function
    return callLimiter
