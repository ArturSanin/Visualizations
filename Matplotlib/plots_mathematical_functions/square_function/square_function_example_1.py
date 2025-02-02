import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-3, 3, 0.01)
y = np.square(x)

fig, ax = plt.subplots()

ax.plot(x, y)  # Plots the x and y values.

plt.xlim(-3, 3)  # Sets the x limits of the axis.
plt.ylim(0, 9)  # Sets the y limits of the axis.
# plt.axis((-3, 3, 0, 9))  # Sets the x and y limits of the axis. (xlimit-left, xlimit-right, ylimit-left, ylimit-right)
plt.axvline(color="grey")  # Adds a vertical grey line at (0, 0).
plt.grid(True)  # Enables grid in the background.

plt.title('Square Function')  # Plot title.
plt.xlabel('x')  # x-axis label.
plt.ylabel('y')  # y-axis label.
plt.show()
