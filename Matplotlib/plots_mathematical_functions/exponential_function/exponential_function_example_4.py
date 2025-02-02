import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-6, 10, 0.01)

fig, ax = plt.subplots()

ax.plot(x, (-1) * np.exp(x), '-r', x, np.exp(x))  # Plots the x and y values.

plt.xlim(-6, 6)  # Sets the x limits of the axis.
plt.ylim(-6, 6)  # Sets the y limits of the axis.
plt.axvline(color="grey")  # Adds vertical line at (0, 0)
plt.axhline(color="grey")  # Adds vertical line at (0, 0)
plt.grid(True)

plt.title('Exponential Functions')  # Plot title.
plt.xlabel('x')  # x-axis label.
plt.ylabel('y')  # y-axis label.
plt.text(2.2, 4.2, r'$y=exp(x)$')  # Adding text to the plot.
plt.text(2.2, -3.8, r'$y=-exp(x)$')  # Adding text to the plot.

plt.show()
