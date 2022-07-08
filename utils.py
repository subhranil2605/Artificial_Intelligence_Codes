import numpy as np


def is_in(elt, seq):
    """Similar to (elt in seq), but compares with 'is', not '=='."""
    return any(x is elt for x in seq)


def probability(p):
    return p > np.random.uniform(0.0, 1.0)
