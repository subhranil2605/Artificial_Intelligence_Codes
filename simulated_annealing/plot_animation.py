import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sa import simulated_annealing

import mplcyberpunk
plt.style.use("cyberpunk")


def obj_func(x):
    return 100 * np.sin(x) / x

class UpdateDist:
    def __init__(self, ax, x, ts, bound):
        self.points, = ax.plot([], [], 'o', zorder=3)
        self.x = x
        self.ts = ts
        self.ax = ax

        # Set up plot parameters
        self.ax.set_xlim(bound[0], bound[1])


    def __call__(self, i):
        # This way the plot can continuously run and we just keep
        # watching new realizations of the process

        if i >= len(self.x):
            return -1

        y = obj_func(self.x[i])
        
        self.points.set_data(self.x[i], y)
        self.ax.set_title(f"Temp={self.ts[i]:0.2f}")
        return self.points,


fig, ax = plt.subplots()

# params
bounds = [0.00001, 21]
bs_size = 8
max_temp, min_temp = 500000, 10
m_iter = 75
perturb_prob = 0.6
k_b = 1.380649e-3

# best solutions and temps
xs, ts = simulated_annealing(obj_func, bounds, bs_size, max_temp, min_temp, m_iter, perturb_prob, k_b, plot=False)

# updating new data each time
ud = UpdateDist(ax, xs, ts, bounds)

# animation
anim = FuncAnimation(fig, ud, frames=len(xs), interval=300, repeat=False)


val = np.linspace(bounds[0], bounds[1], 1000)
ax.plot(val, obj_func(val), zorder=1)

plt.show()
