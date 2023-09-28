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
    return ''.join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """\
------------------------------------------------------------------------------
    Student:
        Represents a student.

    Attributes:
        name (str): The first name of the student.
        surname (str): The last name of the student.
        active (bool, optional): Status of the student (default is True).
        student_login (str): The student's login derived from their name.
        student_id (str): The student's unique generated ID.
------------------------------------------------------------------------------\
    """
    name: str
    surname: str
    active: bool = field(default=True)
    student_login: str = field(init=False)
    student_id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """
        Initialize the student's login based on their name.
        Raise an error if 'id' attribute is passed during initialization.
        """
        self.student_login = self.name[0].capitalize() + self.surname
