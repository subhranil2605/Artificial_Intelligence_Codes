import numpy as np
import sys
import matplotlib.pyplot as plt


INIFINITY = sys.maxsize


def make_binary_string(size):
    return ''.join(map(str, np.random.randint(2, size=size)))


def bin_to_dec_map(binary_str: str, bounds: list):
    """
    Convert binary string to a decimal value and map to a given bouds
    
    """
    
    decoded_value = int(binary_str, 2)
    value = bounds[0] + ((bounds[1] - bounds[0]) / (np.power(2, len(binary_str)) - 1)) * decoded_value
    return value


def perturb(state: str, prob: float) -> str:
    s: list = list(map(int, state))
    
    for pos in range(len(s)):
        if np.random.random() < prob:
            s[pos] = int(not s[pos])

    return ''.join(map(str, s))

        
    
def simulated_annealing(objective,
                        bounds,
                        t_max, t_min,
                        max_iter=10,
                        perturb_prob=0.6,
                        k=0.7) -> None:

    # random initial state
    current_state: str = make_binary_string(8)

    # Initial energy
    current_energy: float = objective(bin_to_dec_map(current_state, bounds))

    # initial large temperature
    T = t_max


    # plotting helpers
    ts = [T]
    es = [current_energy]
    bs = [bin_to_dec_map(current_state, bounds)]

    # run until temperature reduces to a minimum value
    while T > t_min:

        # staying at that temperature for 
        for _ in range(max_iter):

            # new state from the initial state using purturb
            next_state = perturb(current_state, perturb_prob)

            # calculate the energy of the new state
            next_energy = objective(bin_to_dec_map(next_state, bounds))

            # difference between new and old state's energies
            delta_energy = next_energy - current_energy

            # check if the difference is less than equal to 0
            # or in prob e^(- delE / kT)
            # means the successor is better than parent and it is minimization problem
            if delta_energy <= 0 or np.random.random() < np.exp(- delta_energy / (k * T)):
                
                # old state is the new state
                current_state = next_state

                # old energy is the new energy
                current_energy = next_energy


        # cooling temperature
        T *= 0.9
        
        ts.append(T)
        es.append(current_energy)
        bs.append(bin_to_dec_map(current_state, bounds))


    best_sol = bin_to_dec_map(current_state, bounds)
    print(best_sol)

    return bs, ts


##    plt.subplot(2, 1, 1)
##    plt.plot(ts, es)
##    
##    plt.xlim(t_max, t_min)
##    plt.xlabel("T")
##    plt.ylabel("E")
##
##
##    x = np.linspace(bounds[0], bounds[1], 1000)
##    plt.subplot(2, 1, 2)
##    plt.plot(x, objective(x), zorder=1)
##    plt.scatter(best_sol, objective(best_sol), c='r', zorder=3)
##    
##    plt.show()

    
if __name__ == '__main__':
    bounds = [0.00001, 21]
    
    def obj_func(x):
        return 100 * np.sin(x) / x
    
    max_temp = 500000
    min_temp = 10
    m_iter = 50
    perturb_prob = 0.3
    k = 0.3
    
    simulated_annealing(obj_func, bounds, max_temp, min_temp, m_iter, perturb_prob, k)
    
