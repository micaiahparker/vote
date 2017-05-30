from .population import Population, Candidates


class Simulation:
    def __init__(self, n_people=100, n_candidates=5):
        self.population = Population(size=n_people)
        self.candidates = Candidates(size=n_candidates)

    def vote(self):
        votes = {}
        for person in self.population:
            vote = person.vote(candidates.people)[0]
            if vote not in votes:
                votes[vote] = 0
            votes[vote] += 1
        return [dict(name=vote.name, count=votes[vote]) for vote in votes]

    @property
    def data(self):
        return self.population.data + self.candidates.data
