from main import *
import numpy as np
import sys


def exp_schedule(k=20, lam=0.005, limit=100):
    return lambda t: (k * np.exp(-lam * t) if t < limit else 0)


def simulated_annealing(problem, schedule=exp_schedule()):
    states = []
    current = Node(problem.initial)
    for t in range(sys.maxsize):
        states.append(current.state)
        T = schedule(t)
        if T == 0:
            return states
        neighbours = current.expand(problem)
        if not neighbours:
            return current.state
        next_choice = np.random.choice(neighbours)
        delta_e = problem.value(next_choice.state) - problem.value(current.state)
        if delta_e > 0 or probability(np.exp(delta_e / T)):
            current = next_choice
