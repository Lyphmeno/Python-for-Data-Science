#!/usr/bin/env python3.10

from S1E7 import Baratheon, Lannister

class   King(Baratheon, Lannister):
    """
    A class representing a king, inheriting from both Baratheon and Lannister.

    Attributes:
        first_name (str): The first name of the king character.
        is_alive (bool): A flag indicating if the king character is alive.
        family_name (str): The family name "Baratheon".
        eyes (str): The eye color of the king character.
        hairs (str): The hair color of the king character.

    Methods:
        __init__(first_name, is_alive=True): Initialize a king character.
        set_eyes(color): Set the eye color of the king.
        set_hairs(color): Set the hair color of the king.
        get_eyes(): Get the eye color of the king.
        get_hairs(): Get the hair color of the king.
    """
    def __init__(self, first_name, is_alive = True):
        """
        Initialize a king character.

        Args:
            first_name (str): The first name of the character.
            is_alive (bool, optional): A flag indicating if the character is alive.
        """
        super()._init(first_name)

    def set_eyes(self, color):
        """
        Set the eye color of the king.

        Args:
            color (str): The new eye color.
        """
        self.eyes = color

    def set_hairs(self, color):
        """
        Set the hair color of the king.

        Args:
            color (str): The new hair color.
        """
        self.hairs = color

    def get_eyes(self):
        """
        Get the eye color of the king.

        Returns:
            str: The eye color.
        """
        return self.eyes

    def get_hairs(self):
        """
        Get the hair color of the king.

        Returns:
            str: The hair color.
        """
        return self.hairs
