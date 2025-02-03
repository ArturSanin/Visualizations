import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-5, 5, 0.01)
y_1 = np.ceil(x)
y_2 = np.floor(x)

fig, ax = plt.subplots()

ax.plot(x, y_1, x, y_2)  # Plots the x and y values.

plt.xlim(np.min(x), np.max(x))  # Sets the x limits of the axis.
plt.xticks(np.arange(np.min(x), np.max(x), step=1))
plt.ylim(np.min([np.min(y_1), np.min(y_2)]), np.max([np.max(y_1), np.max(y_2)]))  # Sets the y limits of the axis.
plt.yticks(np.arange(np.min([np.min(y_1), np.min(y_2)]), np.max([np.max(y_1), np.max(y_2)]), step=1))
plt.grid(True)  # Enables grid in the background.

plt.title('Ceil and Floor Functions')  # Plot title.
plt.xlabel('x')  # x-axis label.
plt.ylabel('y')  # y-axis label.
plt.text(3.1, 2.1, r'$floor$')
plt.text(2, 3.2, r'$Ceil$')

plt.show()
