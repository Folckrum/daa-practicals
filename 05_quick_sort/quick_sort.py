import random
import sys
import time

sys.setrecursionlimit(10000)
comparisons = 0


def partition(arr, low, high):
    global comparisons
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high, randomized):
    if low < high:
        if randomized:
            r = random.randint(low, high)
            arr[r], arr[high] = arr[high], arr[r]
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1, randomized)
        quick_sort(arr, p + 1, high, randomized)


n = 1000
tests = {
    "Random data": [random.randint(1, 10000) for _ in range(n)],
    "Sorted data (worst case for deterministic)": list(range(n)),
}

for name, data in tests.items():
    print("\n" + name)
    for randomized in (False, True):
        arr = data.copy()
        comparisons = 0
        start = time.time()
        quick_sort(arr, 0, len(arr) - 1, randomized)
        t = time.time() - start
        label = "Randomized   " if randomized else "Deterministic"
        print(f"{label} -> comparisons: {comparisons}, time: {t:.5f}s")
