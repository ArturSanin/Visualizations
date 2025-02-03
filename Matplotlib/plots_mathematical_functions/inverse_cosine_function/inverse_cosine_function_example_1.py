import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-1, 1, 0.0001)
y = np.arccos(x)

fig, ax = plt.subplots()

ax.plot(x, y)  # Plots the x and y values.

plt.xlim(-2, 2)  # Sets the x limits of the axis.
plt.ylim(-0.5, 3.17)  # Sets the y limits of the axis.
plt.axvline(color="grey")  # Adds vertical line at (0, 0).
plt.axhline(color="grey")  # Adds horizontal line at (0, 0).
plt.grid(True)  # Enables grid in the background.

plt.title('Inverse Cosine Function')  # Plot title.
plt.xlabel('x')  # x-axis label.
plt.ylabel('y')  # y-axis label.
plt.show()
