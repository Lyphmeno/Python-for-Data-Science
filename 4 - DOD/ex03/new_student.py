#!/usr/bin/env python3.10

from dataclasses import dataclass, field
import random
import string

def generate_id():
    """
    Generate a random ID consisting of uppercase letters and digits.

    Returns:
        str: The generated ID.
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))

@dataclass
class Student:
    """
    Represents a student with name, surname, active status, student login,
    and student ID.

    Attributes:
        name (str): The first name of the student.
        surname (str): The last name of the student.
        active (bool, optional): Status of the student (default is True).
        student_login (str): The student's login derived from their name.
        student_id (str): The student's unique generated ID.
    """
    name: str
    surname: str
    active: bool = True
    student_login: str = field(init=False)
    student_id: str = field(default_factory=generate_id)

    def __post_init__(self):
        """
        Initialize the student's login based on their name.
        Raise an error if 'id' attribute is passed during initialization.
        """
        self.student_login = self.name.lower()
        if hasattr(self, 'id'):
            raise TypeError(f"{type(self).__name__}.__init__() got an \
                            unexpected keyword argument 'id'")
