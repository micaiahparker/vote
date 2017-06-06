from .population import Population, RandomPopulation


class Simulation:
    def __init__(self, population, candidates):
        self.population = population
        self.candidates = candidates

    def vote(self):
        ballet = {candidate: 0 for candidate in self.candidates}
        for person in self.population:
            ballet[person.vote(self.candidates)[0]] += 1
        return ballet

    def sorted_candidates(self):
        votes = self.vote()
        return sorted(self.candidates, key=lambda x: votes[x])

    def get_next_round(self):
        if len(self.candidates) > 1:
            return Simulation(self.population, Population(self.sorted_candidates()[1:]))
        raise Exception("Simulation needs more than one candidate to produce a next round.")

    def iter_rounds(self):
        return SimulationIterator(self)


class RandomSimulation(Simulation):
    def __init__(self, n_people=100, n_candidates=5):
        super().__init__(RandomPopulation(n_people),
                         RandomPopulation(n_candidates, is_candidate=True))


class SimulationIterator:
    def __init__(self, sim):
        self.first_sim = sim
        self.current_sim = sim

    def __iter__(self):
        self.current_sim = self.first_sim
        return self

    def __next__(self):
        try:
            sim = self.current_sim
            self.current_sim = self.current_sim.get_next_round()
            return sim
        except Exception:
            raise StopIteration
