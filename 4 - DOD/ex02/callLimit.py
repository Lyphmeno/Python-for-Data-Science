#!/usr/bin/env python3.10


def callLimit(limit: int):
    """
    Create a decorator that limits the number of times a function is called.

    Args:
        limit (int): The maximum allowed number of function calls.

    Returns:
        function: A decorator that enforces the call limit on a function.
    """
    count = [0]

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
            if count[0] < limit:
                count[0] += 1
                result = function(*args, **kwds)
                return result
            else:
                return f"Error: {function} call too many times"
        return limit_function
    return callLimiter
