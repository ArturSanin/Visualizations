import matplotlib.pyplot as plt
import numpy as np


def general_sqrt_function(a, b, c, d):
    x = np.arange(- np.divide(c, b), 10, 0.01)
    y = a * np.sqrt(b * x + c) + d
    fig, ax = plt.subplots()

    ax.plot(x, y)  # Plots the x and y values.

    plt.xlim(np.round(np.min(x), 0), np.round(np.max(x), 0))  # Sets the x limits of the axis.
    plt.xticks(np.arange(np.round(np.min(x), 0), np.round(np.max(x), 0), step=1))
    plt.ylim(np.round(np.min(y), 0), np.round(np.max(y), 0))  # Sets the y limits of the axis.
    plt.yticks(np.arange(np.round(np.min(y), 0), np.round(np.max(y), 0), step=1))
    plt.grid(True)  # Enables grid in the background.

    plt.title('General Square Root Function')  # Plot title.
    plt.xlabel('x')  # x-axis label.
    plt.ylabel('y')  # y-axis label.

    plt.show()


general_sqrt_function(2, 0.5, 2, -1)
