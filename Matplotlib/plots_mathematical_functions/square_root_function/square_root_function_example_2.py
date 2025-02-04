import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 10, 0.01)
y_1 = np.sqrt(x)
y_2 = np.sqrt(x - 1)
y_3 = np.sqrt(x - 2)
y_4 = np.sqrt(x - 3)
y_5 = np.sqrt(x - 4)
y_6 = np.sqrt(x - 5)

fig, ax = plt.subplots()

ax.plot(x, y_1, x, y_2, x, y_3, x, y_4, x, y_5, x, y_6)  # Plots the x and y values.

plt.xlim(np.min(x), np.max(x))  # Sets the x limits of the axis.
plt.xticks(np.arange(np.min(x), np.max(x), step=1))
plt.ylim(np.min(y_1), 4.5)  # Sets the y limits of the axis.
plt.yticks(np.arange(np.min(y_1), 4.5, step=1))
plt.grid(True)  # Enables grid in the background.

plt.title('Square Root Functions')  # Plot title.
plt.xlabel('x')  # x-axis label.
plt.ylabel('y')  # y-axis label.

plt.show()
