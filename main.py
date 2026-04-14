from __future__ import annotations

from src.int_list import IntList
from src.sorting_algorithms import Algorithms


def run_sorting(method_name: str, raw_values: list[int], expected: list[int]) -> None:
    values: IntList = IntList(raw_values)
    algorithms: Algorithms = Algorithms(values=values)

    print(f"{method_name}")
    print(f"Before: {algorithms.values}")

    try:
        # 🔥 Dynamically call the method
        getattr(algorithms, method_name)()
    except AttributeError:
        raise ValueError(f"Unknown algorithm: {method_name}")

    print(f"After:  {algorithms.values}")

    if algorithms.values.to_list() != expected:
        raise AssertionError(
            f"{method_name} failed: expected {expected}, got {algorithms.values.to_list()}"
        )

    print("Result: PASS\n")


def main() -> None:
    values: list[int] = [5, 1, 4, 2, 8, 2]

    expected_asc = sorted(values)
    expected_desc = sorted(values, reverse=True)

    tests = [
        ("bubbleSortAscending", expected_asc),
        ("bubbleSortDescending", expected_desc),
        ("selectionSortAscending", expected_asc),
        ("selectionSortDescending", expected_desc),
        ("insertionSortAscending", expected_asc),
        ("insertionSortDescending", expected_desc),
        ("cocktailSortAscending", expected_asc),
        ("cocktailSortDescending", expected_desc),
    ]

    for method_name, expected in tests:
        run_sorting(method_name, values, expected)


if __name__ == "__main__":
    main()