import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0.001, 5, 0.01)
y = []  # List for storing the y-values of the Gamma function.

# Loop to store the corresponding y-values for the x-values.
for v in x:
    y.append(math.gamma(v))

fig, ax = plt.subplots()

ax.plot(x, y)

plt.xlim(-1, 7)  # Sets the x limits of the axis.
plt.ylim(0, 8)  # Sets the y limits of the axis.
plt.axvline(color="grey")  # Adding a vertical line at (0, 0).
plt.axhline(color="grey")  # Adding a horizontal line at (0, 0).
plt.grid(True)  # Enables grid in the background.

plt.title('Gamma function on the positive x-axis')  # Plot title.
plt.xlabel('x')  # x-axis label.
plt.ylabel('y')  # y-axis label.
plt.show()
