from math import sqrt
from random import uniform
from .utils import distance, normalizer

normalize = normalizer(0, sqrt(8))

class Alignment:
    def __init__(self, state=None, moral=None):
        self.state = state or uniform(-1, 1)
        self.moral = moral or uniform(-1, 1)

    @property
    def description(self):
        state, moral = self._str_state(), self._str_moral()
        if state == moral:
            return 'True Neutral'
        return '{state} {moral}'.format(state=state, moral=moral)

    def __repr__(self):
        return self.description

    def opinion(self, alignment):
        return normalize(distance(self.position, alignment.position))

    def _str_state(self):
        if self.state <= -(1/3):
            return 'Chaotic'
        if -(1/3) < self.state < (1/3):
            return 'Neutral'
        if (1/3) <= self.state:
            return 'Lawful'

    def _str_moral(self):
        if self.moral <= -(1/3):
            return 'Evil'
        if -(1/3) < self.moral < (1/3):
            return 'Neutral'
        if (1/3) <= self.moral:
            return 'Good'

    @property
    def position(self):
        return self.state, self.moral
