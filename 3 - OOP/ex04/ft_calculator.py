#!/usr/bin/env pytho


class calculator():
    """
    A class representing a calculator for vector operations.

    Methods:
        dot_product(V1, V2): Calculate the dot product of two vectors.
        add_vec(V1, V2): Add two vectors element-wise.
        subtract_vec(V1, V2): Subtract the vectors element-wise.
    """
    @classmethod
    def dotproduct(cls, V1: list[float], V2: list[float]) -> None:
        """
        Calculate the dot product of two vectors.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        print(sum(x * y for x, y in zip(V1, V2)))

    @classmethod
    def add_vec(cls, V1: list[float], V2: list[float]) -> None:
        """
        Add two vectors element-wise.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        print([x + y for x, y in zip(V1, V2)])

    @classmethod
    def sous_vec(cls, V1: list[float], V2: list[float]) -> None:
        """
        Subtract the second vector from the first vector element-wise.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        print([x - y for x, y in zip(V1, V2)])
