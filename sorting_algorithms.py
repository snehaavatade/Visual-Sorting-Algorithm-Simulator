
def bubble_sort(arr):
    arr = arr.copy()
    history = []
    comparisons = 0
    swaps = 0

    history.append({"array": arr.copy(), "active": []})

    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1

            history.append({
                "array": arr.copy(),
                "active": [j, j + 1]
            })

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

                history.append({
                    "array": arr.copy(),
                    "active": [j, j + 1]
                })

    history.append({"array": arr.copy(), "active": []})

    return history, comparisons, swaps


def selection_sort(arr):
    arr = arr.copy()
    history = []
    comparisons = 0
    swaps = 0

    history.append({"array": arr.copy(), "active": []})

    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1

            history.append({
                "array": arr.copy(),
                "active": [min_index, j]
            })

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

            history.append({
                "array": arr.copy(),
                "active": [i, min_index]
            })

    history.append({"array": arr.copy(), "active": []})

    return history, comparisons, swaps


def insertion_sort(arr):
    arr = arr.copy()
    history = []
    comparisons = 0
    swaps = 0

    history.append({"array": arr.copy(), "active": []})

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            history.append({
                "array": arr.copy(),
                "active": [j, j + 1]
            })

            if arr[j] > key:
                arr[j + 1] = arr[j]
                swaps += 1

                history.append({
                    "array": arr.copy(),
                    "active": [j, j + 1]
                })

                j -= 1
            else:
                break

        arr[j + 1] = key

        history.append({
            "array": arr.copy(),
            "active": [j + 1]
        })

    history.append({"array": arr.copy(), "active": []})

    return history, comparisons, swaps


def merge_sort(arr):
    arr = arr.copy()
    history = []
    comparisons = 0
    swaps = 0

    history.append({"array": arr.copy(), "active": []})

    def merge(left, middle, right):
        nonlocal comparisons, swaps

        left_part = arr[left:middle + 1]
        right_part = arr[middle + 1:right + 1]

        i = 0
        j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            comparisons += 1

            history.append({
                "array": arr.copy(),
                "active": [left + i, middle + 1 + j]
            })

            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1

            swaps += 1

            history.append({
                "array": arr.copy(),
                "active": [k]
            })

            k += 1

        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1
            swaps += 1

            history.append({
                "array": arr.copy(),
                "active": [k - 1]
            })

        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1
            swaps += 1

            history.append({
                "array": arr.copy(),
                "active": [k - 1]
            })

    def divide(left, right):
        if left < right:
            middle = (left + right) // 2

            divide(left, middle)
            divide(middle + 1, right)
            merge(left, middle, right)

    divide(0, len(arr) - 1)

    history.append({"array": arr.copy(), "active": []})

    return history, comparisons, swaps


def quick_sort(arr):
    arr = arr.copy()
    history = []
    comparisons = 0
    swaps = 0

    history.append({"array": arr.copy(), "active": []})

    def partition(low, high):
        nonlocal comparisons, swaps

        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            comparisons += 1

            history.append({
                "array": arr.copy(),
                "active": [j, high]
            })

            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1

                history.append({
                    "array": arr.copy(),
                    "active": [i, j]
                })

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1

        history.append({
            "array": arr.copy(),
            "active": [i + 1, high]
        })

        return i + 1

    def sort(low, high):
        if low < high:
            pivot_index = partition(low, high)

            sort(low, pivot_index - 1)
            sort(pivot_index + 1, high)

    sort(0, len(arr) - 1)

    history.append({"array": arr.copy(), "active": []})

    return history, comparisons, swaps


def run_sorting_algorithm(arr, algorithm):
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    if algorithm not in algorithms:
        raise ValueError("Invalid sorting algorithm")

    return algorithms[algorithm](arr)
