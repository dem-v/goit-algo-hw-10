import random
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


def is_inside(w, h, x, y):
    """Перевіряє, чи знаходиться точка (x, y) всередині трикутника."""
    return y <= (h / w) * x


def is_inside_func(x, y, func_with_bounds):
    """Перевіряє, чи знаходиться точка (x, y) всередині трикутника."""
    func, lbnd, ubnd = func_with_bounds
    return func(x) >= y + func(lbnd) >= func(lbnd) and ubnd >= x + lbnd >= lbnd


def create_plot(f, lbound, ubound):
    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(lbound, ubound)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.7)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=lbound, color='gray', linestyle='--')
    ax.axvline(x=ubound, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(lbound) + ' до ' + str(ubound))
    plt.grid()
    plt.show()


def monte_carlo_simulation(a, b, num_experiments, num_points, func_with_bounds=None):
    """Виконує серію експериментів методом Монте-Карло."""
    average_area = 0

    for _ in range(num_experiments):
        # Генерація випадкових точок
        points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(num_points)]
        # Відбір точок, що знаходяться всередині трикутника
        if func_with_bounds is None or len(func_with_bounds) != 3:
            inside_points = [point for point in points if is_inside(a, b, point[0], point[1])]
        else:
            inside_points = [point for point in points if is_inside_func(point[0], point[1], func_with_bounds)]

        # Розрахунок площі за методом Монте-Карло
        M = len(inside_points)
        N = len(points)
        area = (M / N) * (a * b)

        # Додавання до середньої площі
        average_area += area

    # Обчислення середньої площі
    average_area /= num_experiments
    return average_area


def return_quad(f, a, b):
    return spi.quad(f, a, b)
