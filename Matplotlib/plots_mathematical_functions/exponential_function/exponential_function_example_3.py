import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-6, 10, 0.01)
y = 0.5 * np.exp(0.5 * x - 1) + 2

fig, ax = plt.subplots()

ax.plot(x, y)  # Plots the x and y values.

plt.xlim(-6, 10)  # Sets the x limits of the axis.
plt.ylim(0, 10)  # Sets the y limits of the axis.
plt.axvline(color="grey")  # Adds vertical line at (0, 0)
plt.grid(True)

plt.title('Exponential Function')  # Plot title.
plt.xlabel('x')  # x-axis label.
plt.ylabel('y')  # y-axis label.
plt.show()
