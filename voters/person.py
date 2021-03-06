from random import choice
from names import get_full_name
from .alignment import Alignment


class Person:
    def __init__(self, name=None, alignment=None, is_candidate=False):
        self.name = name
        if is_candidate:
            self.name =  get_full_name()
        self.alignment = alignment or Alignment()
        self.is_candidate = is_candidate

    def opinion(self, person):
        return self.alignment.opinion(person.alignment)

    def vote(self, population):
        return sorted(population, key=self.opinion)

    @property
    def position(self):
        return self.alignment.position

    def __repr__(self):
        return '{name}: {alignment}'.format(name=self.name, alignment=self.alignment)
