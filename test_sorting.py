
from sorting_algorithms import run_sorting_algorithm

numbers = [45, 12, 78, 23, 9, 56]

algorithms = [
    "Bubble Sort",
    "Selection Sort",
    "Insertion Sort",
    "Merge Sort",
    "Quick Sort"
]

print("SORTING ALGORITHM TEST")
print("----------------------")

for algorithm in algorithms:
    history, comparisons, swaps = run_sorting_algorithm(
        numbers, algorithm
    )

    sorted_array = history[-1]["array"]

    print("\nAlgorithm:", algorithm)
    print("Original Array:", numbers)
    print("Sorted Array:", sorted_array)
    print("Comparisons:", comparisons)
    print("Swaps / Movements:", swaps)

    assert sorted_array == sorted(numbers)

print("\nAll algorithms are working correctly!")
