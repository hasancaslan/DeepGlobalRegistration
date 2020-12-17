import random


def get_random_color():
    return [
        round(random.uniform(0.0, 1.0), 1),
        round(random.uniform(0.0, 1.0), 1),
        round(random.uniform(0.0, 1.0), 1)
    ]