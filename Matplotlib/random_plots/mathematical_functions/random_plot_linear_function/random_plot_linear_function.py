"""
    Description: This program generates a random plot of a linear function
    f(x) = a * x + b.
"""

import matplotlib.pyplot as plt
import numpy as np


def random_linear_plot():
    if (2 * np.random.randint(2) - 1) > 0:  # Random condition.

        a = (2 * np.random.randint(2) - 1) * np.random.randint(10)
        b = (2 * np.random.randint(2) - 1) * np.random.randint(10)

        if a == 0:

            x = np.linspace(- 5, 5, 100)
            y = []

            counter_1 = 0

            while counter_1 < len(x):
                y.append(b)
                counter_1 += 1

            fig, ax = plt.subplots()

            ax.plot(x, y)  # Plots the x and y values.

            plt.xlim(np.min(x), np.max(x))

            plt.title('Plot Linear Function ' + 'y = ' + str(np.round(b, 5)))  # Plot title.
            plt.xlabel('x')  # x-axis label.
            plt.ylabel('y')  # y-axis label.

            plt.show()
        else:
            x = np.linspace(- np.round(np.divide(b, a), 0), 5, 100)
            y = a * x + b

            fig, ax = plt.subplots()

            ax.plot(x, y)  # Plots the x and y values.

            plt.xlim(np.min(x), np.max(x))

            if b > 0:
                plt.title('Plot Linear Function ' + 'y = ' + str(a) + ' * x' + ' + ' + str(b))  # Plot title.
            else:
                plt.title(
                    'Plot Linear Function ' + 'y = ' + str(a) + ' * x' + ' - ' + str(np.absolute(b)))  # Plot title.
            plt.xlabel('x')  # x-axis label.
            plt.ylabel('y')  # y-axis label.

            plt.show()
    else:
        a = (2 * np.random.randint(2) - 1) * np.random.randint(10) * np.random.random_sample()
        b = (2 * np.random.randint(2) - 1) * np.random.randint(10) * np.random.random_sample()

        if a == 0:

            x = np.linspace(- 5, 5, 100)
            y = []

            counter_2 = 0

            while counter_2 < len(x):
                y.append(b)
                counter_2 += 1

            fig, ax = plt.subplots()

            ax.plot(x, y)  # Plots the x and y values.

            plt.xlim(np.min(x), np.max(x))

            plt.title('Plot Linear Function ' + 'y = ' + str(np.round(b, 5)))  # Plot title.
            plt.xlabel('x')  # x-axis label.
            plt.ylabel('y')  # y-axis label.

            plt.show()
        else:
            x = np.linspace(- np.round(np.divide(b, a), 0), 5, 100)
            y = a * x + b

            fig, ax = plt.subplots()

            ax.plot(x, y)  # Plots the x and y values.

            plt.xlim(np.min(x), np.max(x))

            if b > 0:
                plt.title('Plot Linear Function ' + 'y = ' + str(np.round(a, 5)) + ' * x' + ' + '
                          + str(np.round(b, 5)))  # Plot title.
            else:
                plt.title('Plot Linear Function ' + 'y = ' + str(np.round(a, 5)) + ' * x' + ' - '
                          + str(np.absolute(np.round(b, 5))))  # Plot title.

            plt.xlabel('x')  # x-axis label.
            plt.ylabel('y')  # y-axis label.

            plt.show()


random_linear_plot()
