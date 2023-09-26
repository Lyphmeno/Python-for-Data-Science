#!/usr/bin/env pytho


class calculator():
    """\
------------------------------------------------------------------------------
    calculator:
        A class representing a calculator for vector operations.

    Methods:
        dot_product(V1, V2): Calculate the dot product of two vectors.
        add_vec(V1, V2): Add two vectors element-wise.
        subtract_vec(V1, V2): Subtract the vectors element-wise.
------------------------------------------------------------------------------\
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculate the dot product of two vectors.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        print(f"Dot product is\t: {sum(x * y for x, y in zip(V1, V2))}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Add two vectors element-wise.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        print(f"Add Vector is\t: {[float(x + y) for x, y in zip(V1, V2)]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtract the second vector from the first vector element-wise.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        print(f"Sous Vector is\t: {[float(x - y) for x, y in zip(V1, V2)]}")
