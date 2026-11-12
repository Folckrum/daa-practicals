n = int(input("Enter number of items: "))

weights = []
values = []
for i in range(n):
    weights.append(float(input(f"Weight of item {i + 1}: ")))
    values.append(float(input(f"Value of item {i + 1}: ")))
capacity = float(input("Enter knapsack capacity: "))

# best value per unit weight first
order = sorted(range(n), key=lambda i: values[i] / weights[i], reverse=True)

total_value = 0
for i in order:
    if capacity == 0:
        break
    take = min(weights[i], capacity)
    total_value += values[i] * take / weights[i]
    capacity -= take
    print(f"Item {i + 1}: took {take} of {weights[i]}")

print("Maximum value:", total_value)
