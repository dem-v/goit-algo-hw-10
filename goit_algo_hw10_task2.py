from goit_algo_hw10_task2_extras import monte_carlo_simulation, create_plot, return_quad
from timeit import timeit


# Визначення функції та межі інтегрування
def f(x):
    return x ** 2


a = 0  # Нижня межа
b = 2  # Верхня межа

create_plot(f, a, b)

experiments = [10, 100, 500]
points = [100, 500, 1000, 5000, 10000, 15000, 30000]

average_area = 0
w = b-a  # ширина прямокутника
h = f(b) - f(a)  # висота прямокутника
S = return_quad(f, a, b)[0]  # Теоретична площа

print("| Число експериментів | Число точок | Середня площа | Похибка | Час виконання |")
print("|---------------------|-------------|--------------|---------|------------|")
# Виконання симуляції
for num_experiments in experiments:
    for num_points in points:

        tm = timeit('global average_area\naverage_area = monte_carlo_simulation(w, h, num_experiments, num_points, (f, a, b))', globals=globals(), number=1)
        print(f"| {num_experiments} | {num_points} | {average_area:.4f} | {abs(S - average_area)/S * 100:.2f}% | {tm:.4f} |")

"""
# Кількість експериментів
num_experiments = 1000
num_points = 1500


# Виконання симуляції
average_area = monte_carlo_simulation(w, h, num_experiments, num_points, (f, a, b))
print(f"Теоретична площа трикутника: {S}")
print(f"Середня площа трикутника за {num_experiments} експериментів: {average_area}")

#print("Інтеграл: ", S)

"""

