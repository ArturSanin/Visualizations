import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
y = np.tan(x)

fig, ax = plt.subplots()

ax.plot(x, y)  # Plots the x and y values.

plt.xlim(-1.6 * np.pi, 1.6 * np.pi)  # Sets the x limits of the axis.
plt.ylim(-2.5, 2.5)  # Sets the y limits of the axis.
plt.axvline(color="grey")  # Adds vertical line at (0, 0).
plt.axhline(color="grey")  # Adds horizontal line at (0, 0).
plt.grid(True)  # Enables grid in the background.

plt.title('Tangent Function')  # Plot title.
plt.xlabel('x')  # x-axis label.
plt.ylabel('y')  # y-axis label.
plt.show()
