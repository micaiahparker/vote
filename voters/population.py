from .person import Person

class Population:
    def __init__(self, size=100, *args, **kwargs):
        self.size = size
        self.people = [Person(*args, **kwargs) for _ in range(self.size)]
    
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
    
    def __len__(self):
        return len(self.people)
    
    @property
    def data(self):
        return [dict(state=p.alignment.state,
                     moral=p.alignment.moral,
                     gender=p.gender,
                     name=p.name,
                     candidate=p.is_candidate,
                     alignment=str(p.alignment)) for p in self.people]
    
class Candidates(Population):
    def __init__(self, size=5, *args, **kwargs):
        super().__init__(size, *args, is_candidate=True, **kwargs)
