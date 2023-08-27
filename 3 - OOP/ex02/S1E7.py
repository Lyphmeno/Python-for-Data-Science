#!/usr/bin/env python3.10

from S1E9 import Character


class Baratheon(Character):
    """
    A subclass of Character representing a member of House Baratheon.

    Attributes:
        first_name (str): The first name of the Baratheon character.
        is_alive (bool): A flag indicating if the Baratheon character is alive.
        family_name (str): The family name "Baratheon".
        eyes (str): The eye color of the Baratheon character -> brown
        hairs (str): The hair color of the Baratheon character -> dark

    Methods:
        die(): Mark the Baratheon character as deceased.
        __str__(): Get a string representation of the Baratheon character.
        __repr__(): Get a string representation of the Baratheon character.
    """
    def __init__(self, first_name, is_alive=True):
        """
        A subclass of Character representing a member of Baratheon Stark.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool): Indicate if the character is alive.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """
        Mark the Baratheon character as deceased.
        """
        super().die()

    def __str__(self):
        """
        Get a string representation of the Baratheon character.

        Returns:
            str: A string representation of the character.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Get a string representation of the Baratheon character.

        Returns:
            str: A string representation of the character.
        """
        return self.__str__()


class Lannister(Character):
    """
    A subclass of Character representing a member of House Lannister.

    Attributes:
        first_name (str): The first name of the Lannister character.
        is_alive (bool): A flag indicating if the Lannister character is alive.
        family_name (str): The family name "Lannister".
        eyes (str): The eye color of the Lannister character -> blue
        hairs (str): The hair color of the Lannister character -> light

    Methods:
        die(): Mark the Lannister character as deceased.
        __str__(): Get a string representation of the Lannister character.
        __repr__(): Get a string representation of the Lannister character.
    """
    def __init__(self, first_name, is_alive=True):
        """
        A subclass of Character representing a member of Lannister Stark.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool): Indicate if the character is alive.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """
        Mark the Lannister character as deceased.
        """
        super().die()

    def __str__(self):
        """
        Get a string representation of the Lannister character.

        Returns:
            str: A string representation of the character.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Get a string representation of the Lannister character.

        Returns:
            str: A string representation of the character.
        """
        return self.__str__()

    @classmethod
    def createLannister(cls, first_name, is_alive=True):
        """
        Class method to create Lannisters characters in a chain.
        """
        return cls(first_name, is_alive)
