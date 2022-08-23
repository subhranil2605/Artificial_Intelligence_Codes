"""
Genetic Algorithm
"""
import matplotlib.pyplot as plt
import mplcyberpunk
import numpy as np

plt.style.use("cyberpunk")

range_ = [10, 30]


def func(x):
    return 100 * np.sin(x) / x


def make_chromosome(size):
    return ''.join(map(str, np.random.randint(2, size=size)))


def make_population(pop_size: int, chrom_length: int):
    return [make_chromosome(chrom_length) for _ in range(pop_size)]


def fitness(chromosome):
    decoded_value = int(chromosome, 2)
    value = range_[0] + ((range_[1] - range_[0]) / (np.power(2, len(chromosome)) - 1)) * decoded_value
    return func(value)


def conversion(chromosome):
    decoded_value = int(chromosome, 2)
    value = range_[0] + ((range_[1] - range_[0]) / (np.power(2, len(chromosome)) - 1)) * decoded_value
    return value


def max_with_index(list_: list):
    max_element = max(list_)
    return max_element, list_.index(max_element)


def binary_tournament(chrom_1, chrom_2):
    return chrom_1 if fitness(chrom_1) >= fitness(chrom_2) else chrom_2


def single_point_crossover(chrom_1, chrom_2):
    assert len(chrom_1) == len(chrom_2), "Different sizes of chromosomes"

    cp = np.random.randint(len(chrom_1))
    child_1 = chrom_1[:cp] + chrom_2[cp:]
    child_2 = chrom_2[:cp] + chrom_1[cp:]
    return child_1, child_2


def selection(population: list):
    mat_pool = []
    while len(mat_pool) <= len(population):
        chrom_1 = population[np.random.randint(len(population))]
        chrom_2 = population[np.random.randint(len(population))]
        best_chrom = binary_tournament(chrom_1, chrom_2)
        mat_pool.append(best_chrom)

    return mat_pool


def crossover(population: list, cross_prob: float):
    xpopulation = []
    parent_1 = population[np.random.randint(len(population))]
    parent_2 = population[np.random.randint(len(population))]

    if np.random.random() < cross_prob:
        child1, child2 = single_point_crossover(parent_1, parent_2)
        xpopulation.extend([child1, child2])
    else:
        xpopulation.extend([parent_1, parent_2])
    return xpopulation


def mutate(chrom: str, mp: float) -> str:
    c = list(map(int, chrom))
    for pos in range(len(c)):
        if np.random.random() < mp:
            c[pos] = int(not c[pos])

    return ''.join(map(str, c))


def mutation(population: list, mut_prob: float) -> None:
    for i, chrom in enumerate(population):
        population[i] = mutate(chrom, mut_prob)


def genetic_algorithm(pop_size, chrom_len, max_iter, cross_prob, mut_prob):
    pop = make_population(pop_size, chrom_len)
    fit = list(map(fitness, pop))
    best_fits = []
    avg_fits = []
    sols = []

    i = 0
    while i < max_iter:
        best_fits.append(max(fit))
        avg_fits.append(np.mean(fit))
        mpool = selection(pop)
        xpop = crossover(mpool, cross_prob)
        mutation(xpop, mut_prob)
        child_best_fit = list(map(fitness, xpop))

        # elitism
        old_best, old_i = max_with_index(fit)
        new_best, new_i = max_with_index(child_best_fit)

        if old_best >= new_best:
            xpop[new_i] = pop[old_i]
            child_best_fit[new_i] = fit[new_i]

        sols.append(conversion(xpop[new_i]))

        pop = xpop
        fit = child_best_fit

        i += 1

    f = list(map(fitness, pop))
    f_max, max_i = max(f), f.index(max(f))
    print(conversion(pop[max_i]), f_max)

    plt.figure(figsize=(12, 8), dpi=200)

    plt.subplot(2, 1, 1)
    plt.plot(avg_fits, label='Avg. Fitness')
    plt.plot(best_fits, label='Best Fitness')
    plt.legend()
    plt.grid()
    plt.title(f"Genetic Algorithm\ncrossover_prob = {cross_prob}, mutation_prob={mut_prob}")

    plt.subplot(2, 1, 2)
    x = np.linspace(range_[0], range_[1], 1000)
    plt.scatter(conversion(pop[max_i]), f_max, c='red', marker='x', s=60, zorder=3)
    plt.scatter(sols, func(sols), c='black', s=4, alpha=0.3, zorder=2)
    plt.plot(x, func(x), zorder=1)
    plt.grid()
    plt.xlabel("$x$")
    plt.ylabel(r"$f(x)=100 \frac{\sin(x)}{x}$")

    plt.savefig(f'ga/ga_{cross_prob}_{mut_prob}.jpg')
    plt.show()


if __name__ == '__main__':
    genetic_algorithm(100, 10, 100, 0.93, 0.01)
