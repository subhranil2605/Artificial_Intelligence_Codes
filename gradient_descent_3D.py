import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


fig = plt.figure()
ax = plt.axes(projection="3d")



# derivate or gradient
def deriv(func, input_, delta=0.001):
    return (func(input_ + delta) - func(input_ - delta)) / (2 * delta)



# gradient descent funtion
def gradient_descent(start, func, learn_rate, max_iter, tol= 0.01):
    steps = [start]
    x = start
    for _ in range(max_iter):
        diff= learn_rate * deriv(func, x)
        if np.abs(diff) < tol:
            break 
        x -= diff
        steps.append(x)

    return steps, x


def func(x, y):
    return 0.5 * np.power(x, 2) + np.power(y, 2)


history_x, result_x = gradient_descent(9, func, 0.1, 100)
history_y, result_y = gradient_descent(11, func, 0.1, 100)



x = y = np.linspace(-2, 2, 100)
xx, yy = np.meshgrid(x, y)
z = func(xx, yy)


ax.plot_surface(xx, yy, z)


plt.show()
