import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Total Qty", pulp.LpMaximize)

# Визначення змінних
A = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
B = pulp.LpVariable('FruitJuice', lowBound=0, cat='Integer')

# Функція цілі
model += A + B, "TotalQty"

# Додавання обмежень
model += 2 * A + B <= 100  # Обмеження води
model += A <= 50  # Обмеження цукру
model += A <= 30  # Обмеження лимонного соку
model += 2 * B <= 40  # Обмеження лимонного соку

# Розв'язання моделі
model.solve()

print(model)

# Вивід результатів
print("Виробляти лимонадів:", A.varValue)
print("Виробляти фруктових соків:", B.varValue)
