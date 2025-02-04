import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 10, 0.01)
y = np.sqrt(x)

fig, ax = plt.subplots()

ax.plot(x, y)  # Plots the x and y values.

plt.xlim(np.min(x), np.max(x))  # Sets the x limits of the axis.
plt.xticks(np.arange(np.min(x), np.max(x), step=1))
plt.ylim(np.min(y), 4.5)  # Sets the y limits of the axis.
plt.yticks(np.arange(np.min(y), 4.5, step=1))
plt.grid(True)  # Enables grid in the background.

plt.title('Square Root Function')  # Plot title.
plt.xlabel('x')  # x-axis label.
plt.ylabel('y')  # y-axis label.

plt.show()
