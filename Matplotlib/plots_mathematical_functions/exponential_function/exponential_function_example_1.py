import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-4, 3, 0.01)
y = np.exp(x)

fig, ax = plt.subplots()

ax.plot(x, y)  # Plots the x and y values.

plt.xlim(-4, 3)  # Sets the x limits of the axis.
plt.ylim(0, 8)  # Sets the y limits of the axis.
plt.axvline(color="grey")  # Adds vertical line at (0, 0)
plt.grid(True)

plt.title('Exponential Function')  # Plot title.
plt.xlabel('x')  # x-axis label.
plt.ylabel('y')  # y-axis label.
plt.show()
