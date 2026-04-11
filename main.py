from __future__ import annotations

from src.int_list import IntList
from src.sorting_algorithms import Algorithms


def run_sorting(algorithm_name: str, raw_values: list[int], expected: list[int]) -> None:
    values: IntList = IntList(raw_values)
    algorithms: Algorithms = Algorithms(values=values)

    print(f"{algorithm_name}")
    print(f"Before: {algorithms.values}")

    if algorithm_name == "bubble_sort_ascending":
        algorithms.bubbleSortAscending()
    elif algorithm_name == "selection_sort_ascending":
        algorithms.selectionSortAscending()
    elif algorithm_name == "insertion_sort_ascending":
        algorithms.insertionSortAscending()
    else:
        raise ValueError(f"Unknown algorithm: {algorithm_name}")

    print(f"After:  {algorithms.values}")

    if algorithms.values.to_list() != expected:
        raise AssertionError(
            f"{algorithm_name} failed: expected {expected}, got {algorithms.values.to_list()}"
        )

    print("Result: PASS\n")


def main() -> None:
    values: list[int] = [5, 1, 4, 2, 8, 2]
    expected: list[int] = sorted(values)

    run_sorting("bubble_sort_ascending", values, expected)
    run_sorting("selection_sort_ascending", values, expected)
    run_sorting("insertion_sort_ascending", values, expected)


if __name__ == "__main__":
    main()
