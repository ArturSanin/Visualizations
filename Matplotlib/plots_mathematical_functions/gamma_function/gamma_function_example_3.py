import matplotlib.pyplot as plt
import numpy as np
import math

x_1 = np.arange(-3.999, -3.01, 0.01)
y_1 = []
for v_1 in x_1:
    y_1.append(math.gamma(v_1))

x_2 = np.arange(-2.99, -2.01, 0.01)
y_2 = []
for v_2 in x_2:
    y_2.append(math.gamma(v_2))

x_3 = np.arange(-1.99, -1.01, 0.01)
y_3 = []
for v_3 in x_3:
    y_3.append(math.gamma(v_3))

x_4 = np.arange(-0.99, -0.01, 0.01)
y_4 = []
for v_4 in x_4:
    y_4.append(math.gamma(v_4))

x_5 = np.arange(0.001, 5, 0.01)
y_5 = []
for v_5 in x_5:
    y_5.append(math.gamma(v_5))

fig, ax = plt.subplots()

ax.plot(x_1, y_1, '#1f77b4', x_2, y_2, '#1f77b4', x_3, y_3, '#1f77b4', x_4, y_4, '#1f77b4', x_5, y_5, '#1f77b4')

plt.xlim(-5, 7)  # Sets the x limits of the axis.
plt.ylim(-8, 8)  # Sets the y limits of the axis.
plt.axvline(color="grey")  # Adding a vertical line at (0, 0).
plt.axhline(color="grey")  # Adding a horizontal line at (0, 0).
plt.grid(True)  # Enables grid in the background.

plt.title('Gamma Function')  # Plot title.
plt.xlabel('x')  # x-axis label.
plt.ylabel('y')  # y-axis label.
plt.show()
