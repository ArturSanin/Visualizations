"""
    Description: This program generates a random plot of a general square root function
    f(x) = a * sqrt{b * x + c} + d.
"""

import matplotlib.pyplot as plt
import numpy as np


def random_sqrt_plot():
    a = (2 * np.random.randint(2) - 1) * np.random.randint(10)
    b = (2 * np.random.randint(2) - 1) * np.random.randint(10) + 1  # Adding 1, so b is not equal to 0.
    c = (2 * np.random.randint(2) - 1) * np.random.randint(10)
    d = (2 * np.random.randint(2) - 1) * np.random.randint(10)

    x = np.arange(- np.round(np.divide(c, b), 0), 5, 0.01)
    y = a * np.sqrt(b * x + c) + d

    fig, ax = plt.subplots()

    ax.plot(x, y)  # Plots the x and y values.

    plt.xlim(np.min(x), np.max(x))

    plt.title('Random Square Root Function')  # Plot title.
    plt.xlabel('x')  # x-axis label.
    plt.ylabel('y')  # y-axis label.

    plt.show()


random_sqrt_plot()
