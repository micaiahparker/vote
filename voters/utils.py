from math import sqrt


def distance(a, b):
    return sqrt(sum(map(lambda x: (x[1]-x[0])**2, zip(a, b))))

def scaler(old_low, old_high, new_low, new_high):
    def func(x):
        old_range = old_high - old_low
        new_range = new_high - new_low
        return (((x - old_low) * new_range) / old_range) + new_low
    return func

def normalizer(old_low, old_high):
    return scaler(old_low, old_high, 0, 1)
