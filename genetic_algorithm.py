"""
Genetic Algorithm
"""
import numpy as np

range_ = [0, 10]


def func(x):
    return x * (8 - x)


def make_chromosome(size):
    return ''.join(map(str, np.random.randint(2, size=size)))


def fitness(chromosome):
    decoded_value = int(chromosome, 2)
    value = range_[0] + ((range_[1] - range_[0]) / (np.power(2, len(chromosome)) - 1)) * decoded_value
    return func(value)


def binary_tournament(chrom_1, chrom_2):
    return chrom_1 if fitness(chrom_1) >= fitness(chrom_2) else chrom_2


def selection():
    mat_pool = []
    while len(mat_pool) <= 10:



def genetic_algorithm():
    pass


if __name__ == '__main__':
    chrom_1 = make_chromosome(8)
    chrom_2 = make_chromosome(8)
    print(chrom_1, chrom_2)
    print(fitness(chrom_1), fitness(chrom_2))
    print(binary_tournament(chrom_1, chrom_2))
