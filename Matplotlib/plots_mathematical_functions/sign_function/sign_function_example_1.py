import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-7, 7, 0.01)
y = np.sign(x)

fig, ax = plt.subplots()

ax.plot(x, y)  # Plots the x and y values.

plt.xlim(np.min(x), np.max(x))  # Sets the x limits of the axis.
plt.xticks(np.arange(np.min(x), np.max(x), step=1))
plt.ylim(np.min(y) - 2, np.max(y) + 2)  # Sets the y limits of the axis.

plt.title('Sign Function')  # Plot title.
plt.xlabel('x')  # x-axis label.
plt.ylabel('y')  # y-axis label.

plt.show()
