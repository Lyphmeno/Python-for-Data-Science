#!/usr/bin/env python3.10

from abc import ABC, asbtractmethod


class Character(ABC):
    """
    An abstract base class representing a character.

    Attributes:
        first_name (str): The first name of the character.
        is_alive (bool): A flag indicating if the character is alive.

    Methods:
        die(): Abstract method to mark the character as deceased.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    @asbtractmethod
    def die(self):
        """Abstract method: Mark the character as deceased."""
        self.is_alive = False


class Stark(Character):
    """
    A subclass of Character representing a member of House Stark.

    Methods:
        die(): Mark the Stark character as deceased.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Mark the Stark character as deceased."""
        super().die()
