def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_loop(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


n = int(input("Enter n: "))

print("Series using recursion:", end=" ")
for i in range(n):
    print(fib_recursive(i), end=" ")

print("\nSeries using loop:     ", end=" ")
for i in range(n):
    print(fib_loop(i), end=" ")

print("\n")
print("Recursion -> time O(2^n), space O(n)")
print("Loop      -> time O(n),   space O(1)")
