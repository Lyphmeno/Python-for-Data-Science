#!/usr/bin/env python3.10

from abc import ABC, abstractmethod


class Character(ABC):
    """\
------------------------------------------------------------------------------
    Character:
        Abstract class representing characters.

    Attributes:
        name (str): character name.
        is_alive (bool): life status.

    Methods:
        die(): set character is_alive status to false.
        exemple(): def.
------------------------------------------------------------------------------\
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Character asbtract class"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method: Mark the character as deceased."""
        self.is_alive = False


class Stark(Character):
    """\
------------------------------------------------------------------------------
    Stark:
        Subclass of Character representing a member of House Stark.

    Methods:
        die(): Mark the Stark character as deceased.
------------------------------------------------------------------------------\
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Stark class (Inherited from Character)"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Mark the Stark character as deceased."""
        super().die()
