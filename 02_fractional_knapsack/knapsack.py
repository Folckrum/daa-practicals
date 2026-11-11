n = int(input("Number of items: "))
items = []
for i in range(n):
    w = float(input(f"Weight of item {i + 1}: "))
    v = float(input(f"Value of item {i + 1}: "))
    items.append((w, v))
capacity = float(input("Knapsack capacity: "))

items.sort(key=lambda x: x[1] / x[0], reverse=True)

total = 0
for w, v in items:
    if capacity >= w:
        total += v
        capacity -= w
    else:
        total += v * (capacity / w)
        break

print("Max value:", total)
