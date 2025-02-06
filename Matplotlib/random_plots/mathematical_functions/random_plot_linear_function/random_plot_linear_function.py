import matplotlib.pyplot as plt
import numpy as np


def random_linear_plot():
    """
        This program generates a random plot of a linear function f(x) = a * x + b.
    """

    # Defining the coefficient of the linear function through a random condition.
    if (2 * np.random.randint(2) - 1) > 0:
        a = (2 * np.random.randint(2) - 1) * np.random.randint(10)
    else:
        a = (2 * np.random.randint(2) - 1) * np.round(np.random.randint(10) * np.random.random_sample(),
                                                      np.random.randint(1, 6))

    if (2 * np.random.randint(2) - 1) > 0:
        b = (2 * np.random.randint(2) - 1) * np.random.randint(10)
    else:
        b = (2 * np.random.randint(2) - 1) * np.round(np.random.randint(10) * np.random.random_sample(),
                                                      np.random.randint(1, 6))

    # Depending on the values of the coefficients, a plot will be displayed.
    if (a == 0) and (b == 0):
        x = np.linspace(- 5, 5, 100)
        y = []

        counter_1 = 0
        while counter_1 < len(x):
            y.append(0)
            counter_1 += 1

        fig, ax = plt.subplots()

        ax.plot(x, y)  # Plots the x and y values.

        plt.xlim(np.min(x), np.max(x))

        plt.title('Plot Linear Function ' + 'y = ' + str(0))  # Plot title.

        # Axis labels.
        plt.xlabel('x')
        plt.ylabel('y')

        plt.show()

    elif a == 0:
        x = np.linspace(- 5, 5, 100)
        y = []

        counter_2 = 0
        while counter_2 < len(x):
            y.append(b)
            counter_2 += 1

        fig, ax = plt.subplots()

        ax.plot(x, y)  # Plots the x and y values.

        plt.xlim(np.min(x), np.max(x))

        plt.title('Plot Linear Function ' + 'y = ' + str(b))  # Plot title.

        # Axis labels.
        plt.xlabel('x')
        plt.ylabel('y')

        plt.show()

    elif b == 0:
        x = np.linspace(0, 5, 100)
        y = a * x

        fig, ax = plt.subplots()

        ax.plot(x, y)  # Plots the x and y values.

        plt.xlim(np.min(x), np.max(x))

        # Displaying the plot title depending on the value of a.
        if a == 1:
            plt.title('Plot Linear Function ' + 'y = ' + 'x')
        elif a == -1:
            plt.title('Plot Linear Function ' + 'y = ' + '-x')
        else:
            plt.title('Plot Linear Function ' + 'y = ' + str(a) + ' * x')

        # Axis labels.
        plt.xlabel('x')
        plt.ylabel('y')

        plt.show()

    else:
        x = np.linspace(- np.round(np.divide(b, a), 0), 5, 100)
        y = a * x + b

        fig, ax = plt.subplots()

        ax.plot(x, y)  # Plots the x and y values.

        plt.xlim(np.min(x), np.max(x))

        # Displaying the plot title depending on the values of a and b.
        if (a == 1) and (b > 0):
            plt.title('Plot Linear Function ' + 'y = ' + 'x' + ' + ' + str(b))
        elif (a == 1) and (b < 0):
            plt.title('Plot Linear Function ' + 'y = ' + 'x' + ' - ' + str(np.absolute(b)))
        elif (a == -1) and (b > 0):
            plt.title('Plot Linear Function ' + 'y = ' + '-x' + ' + ' + str(b))
        elif (a == -1) and (b < 0):
            plt.title('Plot Linear Function ' + 'y = ' + '-x' + ' - ' + str(np.absolute(b)))
        elif b > 0:
            plt.title('Plot Linear Function ' + 'y = ' + str(a) + ' * x' + ' - ' + str(b))
        else:
            plt.title('Plot Linear Function ' + 'y = ' + str(a) + ' * x' + ' - ' + str(np.absolute(b)))

        # Axis labels.
        plt.xlabel('x')
        plt.ylabel('y')

        plt.show()


random_linear_plot()
