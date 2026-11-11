import time


def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


n = int(input("Enter n: "))

start = time.time()
print("Recursive:", fib_recursive(n))
print("Recursive time:", time.time() - start)

start = time.time()
print("Iterative:", fib_iterative(n))
print("Iterative time:", time.time() - start)

print("\nRecursive -> Time: O(2^n), Space: O(n)")
print("Iterative -> Time: O(n),   Space: O(1)")
