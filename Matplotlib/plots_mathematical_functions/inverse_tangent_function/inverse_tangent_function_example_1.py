import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-8, 8, 0.001)
y = np.arctan(x)

fig, ax = plt.subplots()

ax.plot(x, y)  # Plots the x and y values.

plt.xlim(-7, 7)  # Sets the x limits of the axis.
plt.ylim(-0.5 * np.pi - 0.3, 0.5 * np.pi + 0.3)  # Sets the y limits of the axis.
plt.axvline(color="grey")  # Adds vertical line at (0, 0).
plt.axhline(color="grey")  # Adds horizontal line at (0, 0).
plt.grid(True)  # Enables grid in the background.

plt.title('Inverse Tangent Function')  # Plot title.
plt.xlabel('x')  # x-axis label.
plt.ylabel('y')  # y-axis label.
plt.show()
