#!/usr/bin/env python3.10


class calculator():
    """\
------------------------------------------------------------------------------
    calculator:
        Simple calculator for element-wise operations on a list of numbers.

    Attributes:
        values (list): The list of numbers.

    Methods:
        __init__(values): Initialize the calculator with a list of numbers.
        __add__(object) -> list: Perform element-wise addition
        __mul__(object) -> list: Perform element-wise multiplication
        __sub__(object) -> list: Perform element-wise subtraction
        __truediv__(object) -> list: Perform element-wise division
------------------------------------------------------------------------------\
    """
    def __init__(self, object):
        """
        Initialize the calculator with a list of numbers.

        Args:
            values (list): The list of numbers.
        """
        self.object = object

    def __add__(self, object) -> None:
        """
        Perform element-wise addition with an object.

        Args:
            object (float): The object for addition.
        """
        self.object = [x + object for x in self.object]
        print(self.object)

    def __mul__(self, object) -> None:
        """
        Perform element-wise multiplication with an object.

        Args:
            object (float): The object for multiplication.
        """
        self.object = [x * object for x in self.object]
        print(self.object)

    def __sub__(self, object) -> None:
        """
        Perform element-wise subtraction with an object.

        Args:
            object (float): The object for subtraction.
        """
        self.object = [x - object for x in self.object]
        print(self.object)

    def __truediv__(self, object) -> None:
        """
        Perform element-wise division with an object.

        Args:
            object (float): The object for division.

        Raises:
            ValueError: If the provided object is equal to zero.
        """
        if object == 0:
            raise ValueError("Cannot divide by zero")
        self.object = [x / object for x in self.object]
        print(self.object)
