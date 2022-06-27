import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray
from typing import Callable
import matplotlib.animation as animation


# derivate or gradient
def deriv(func: Callable[[float], float],
          input_: ndarray,
          delta:float = 0.001) -> ndarray:
    
    return (func(input_ + delta) - func(input_ - delta)) / (2 * delta)



# gradient descent funtion
def gradient_descent(start: float,
                     func: Callable[[float], float],
                     learn_rate: float,
                     max_iter: int,
                     tol:float = 0.01) -> tuple[list[float], float]:
    
    steps: list[float] = [start]
    x: float = start

    for _ in range(max_iter):
        diff: float = learn_rate * deriv(func, x)
        
        if np.abs(diff) < tol:
            break
        
        x -= diff
        steps.append(x)

    return steps, x


# function
def func(x):
    return np.power(x, 2) - 4*x + 1


lower_bound = -10
upper_bound = 10
starting_point = np.random.randint(lower_bound, upper_bound)


# result
lr=0.8
history, result = gradient_descent(9, func, lr, 100)

# convering list into array
h = np.array(history)


# data generator function return generator object
def gen_data(d):
    for i in d:
        print(i, func(i))
        yield i, func(i)


x: ndarray = np.linspace(lower_bound, upper_bound, 1000)
y: ndarray = func(x)


fig, ax = plt.subplots()
ax.grid()
x_data, y_data = [], []
line, = ax.plot([], [], lw=3, c="red")
point, = ax.plot([], [], 'k.')

ax.set_xlabel("$x$")
ax.set_ylabel("$x^2-4x+1$")



# animation function
def run(data):
    t, y = data
    x_data.append(t)
    y_data.append(y)
    ax.figure.canvas.draw()
    line.set_data(x_data, y_data)
    point.set_data(x_data, y_data)
    ax.set_title(f"Gradient Descent\nx={t}, lr={lr}")
    return line, point, 


# function plot
ax.plot(x, y)

# animate this one
ani = animation.FuncAnimation(fig, run, gen_data(h), interval=10, repeat=False)

plt.show()
