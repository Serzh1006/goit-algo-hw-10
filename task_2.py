import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


def monte_carlo_area(f, x_min, x_max, N):
    x_random = np.random.uniform(x_min, x_max, N)
    y_random = np.random.uniform(0, f(x_max), N)
    under_curve = y_random < f(x_random)
    fraction_under_curve = np.mean(under_curve)
    rect_area = (x_max - x_min) * f(x_max)
    area_under_curve = fraction_under_curve * rect_area

    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    _, ax = plt.subplots()

    ax.plot(x, y, 'r', linewidth=2)

    ix = np.linspace(x_min, x_max)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    ax.axvline(x=x_min, color='gray', linestyle='--')
    ax.axvline(x=x_max, color='gray', linestyle='--')

    result, _ = spi.quad(f, x_min, x_max)
    print(f"Інтеграл: {result:0.5f}")
    plt.scatter(x_random, y_random, c='blue', s=10)
    plt.title('Графік інтегрування f(x) = x^2 від ' + str(x_min) + ' до ' + str(x_max))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()
    return area_under_curve


def f(x):
    return x**2

x_min, x_max = 0, 2
N = 1000

for N in [10,100,1000,10000]:
    print(f"N = {N}")
    estimated_area = monte_carlo_area(f, x_min, x_max, N)
    print(f"Площа методом Монте-Карло: {estimated_area}")