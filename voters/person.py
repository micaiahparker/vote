from random import choice
from names import get_full_name
from .alignment import Alignment


class Person:
    def __init__(self, name=None, alignment=None):
        self.gender = choice(['male', 'female'])
        self.name = name or get_full_name(gender=self.gender)
        self.alignment = alignment or Alignment()

    def opinion(self, person):
        return self.alignment.opinion(person.alignment)

    def vote(self, people):
        return sorted(people, key=self.opinion)

    @property
    def position(self):
        return self.alignment.position

    def __repr__(self):
        return f'{self.name}: {self.alignment}'

