import pulp

model = pulp.LpProblem("maximize-drinks-production", pulp.LpMaximize)

limonad = pulp.LpVariable(name="limonad", lowBound=0, cat="Integer")
fruit_juice = pulp.LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

model += (2 * limonad + 1 * fruit_juice <= 100, "water_constraint")
model += (1 * limonad <= 50, "sugar_constraint")
model += (1 * limonad <= 30, "lemon_juice_constraint")
model += (2 * fruit_juice <= 40, "fruit_puree_constraint")

model += pulp.lpSum([limonad, fruit_juice])
model.solve()

print(f"Optimal number of 'Limonad' to produce: {limonad.value()}")
print(f"Optimal number of 'Fruit Juice' to produce: {fruit_juice.value()}")
print(f"status = {pulp.LpStatus[model.status]}")