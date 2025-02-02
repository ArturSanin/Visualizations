import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-10, 10, 0.01)

fig, ax = plt.subplots()

ax.plot(x, np.square(x + 2), '-m', x, np.square(x + 1), '-c', x, np.square(x), '-b',
        x, np.square(x - 1), '-r', x, np.square(x - 2), '-g')  # Plots the x and y values.

plt.xlim(-5, 5)  # Sets the x limits of the axis.
plt.ylim(0, 9)  # Sets the y limits of the axis.
# plt.axis((-3, 3, 0, 9))  # Sets the x and y limits of the axis. (xlimit-left, xlimit-right, ylimit-left, ylimit-right)
plt.axvline(color="grey")  # Adds a vertical grey line at (0, 0).
plt.grid(True)  # Enables grid in the background.

plt.title('Square Functions')  # Plot title.
plt.xlabel('x')  # x-axis label.
plt.ylabel('y')  # y-axis label.
plt.show()
