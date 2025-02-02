import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-4, 5, 0.01)

fig, ax = plt.subplots()

ax.plot(x, np.exp(x + 2), x, np.exp(x + 1), x, np.exp(x),
        x, np.exp(x - 1), x, np.exp(x - 2))  # Plots the x and y values.

plt.xlim(-4, 5)  # Sets the x limits of the axis.
plt.ylim(0, 8)  # Sets the y limits of the axis.
plt.axvline(color="grey")  # Adds vertical line at (0, 0)
plt.grid(True)

plt.title('Exponential Function')  # Plot title.
plt.xlabel('x')  # x-axis label.
plt.ylabel('y')  # y-axis label.
plt.show()
