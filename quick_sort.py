import random

count = 0   # number of comparisons


def partition(arr, low, high):
    global count
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        count += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


def randomized_quick_sort(arr, low, high):
    if low < high:
        r = random.randint(low, high)
        arr[r], arr[high] = arr[high], arr[r]
        p = partition(arr, low, high)
        randomized_quick_sort(arr, low, p - 1)
        randomized_quick_sort(arr, p + 1, high)


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

arr = numbers.copy()
count = 0
quick_sort(arr, 0, len(arr) - 1)
print("Deterministic:", arr, "| comparisons:", count)

arr = numbers.copy()
count = 0
randomized_quick_sort(arr, 0, len(arr) - 1)
print("Randomized:   ", arr, "| comparisons:", count)

print()
print("Deterministic -> best/average O(n log n), worst O(n^2) (e.g. already sorted input)")
print("Randomized    -> expected O(n log n) for any input")
