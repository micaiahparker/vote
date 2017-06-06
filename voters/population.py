from .person import Person
from .alignment import Alignment


class Population:
    def __init__(self, people):
        self.people = people

    @property
    def size(self):
        return len(self.people)

    def __iter__(self):
        return iter(self.people)

    @property
    def position(self):
        return self.state, self.moral

    @property
    def state(self):
        return sum(map(lambda x: x.alignment.state, self.people)) / self.size

    @property
    def moral(self):
        return sum(map(lambda x: x.alignment.moral, self.people)) / self.size

    def opinion(self, person):
        return sum(map(lambda x: x.opinion(person), self.people)) / self.size

    def __len__(self):
        return len(self.people)

    @property
    def data(self):
        return [dict(state=p.alignment.state,
                     moral=p.alignment.moral,
                     name=p.name,
                     candidate=p.is_candidate,
                     alignment=str(p.alignment)) for p in self.people]


class RandomPopulation(Population):
    def __init__(self, n_people, *args, **kwargs):
        super().__init__([Person(*args, **kwargs) for person in range(n_people)])
