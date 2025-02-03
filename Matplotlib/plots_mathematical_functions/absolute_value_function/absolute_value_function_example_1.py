import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-5, 5, 0.01)
y = np.absolute(x)

fig, ax = plt.subplots()

ax.plot(x, y)  # Plots the x and y values.

plt.xlim(np.min(x), np.max(x))  # Sets the x limits of the axis.
plt.xticks(np.arange(np.min(x), np.max(x), step=1))
plt.ylim(np.min(y) - 1, np.max(y) + 1)  # Sets the y limits of the axis.

plt.title('Absolute Value Function')  # Plot title.
plt.xlabel('x')  # x-axis label.
plt.ylabel('y')  # y-axis label.

plt.show()
