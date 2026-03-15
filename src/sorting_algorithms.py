from src.int_list import IntList
from beartype import beartype

@beartype
class Algorithms:

    def __init__(self, values: IntList) -> None:
        self.values: IntList = values

    def bubbleSortAscending(self) -> None:
        list_size: int = self.values.size()
        didSwap: bool = True

        while didSwap:
            didSwap = False

            for i in range(0, list_size - 1):
                current: int = self.values.get(i)
                next_value: int = self.values.get(i + 1)

                if current > next_value:
                    self.values.swap(i, i + 1)
                    didSwap = True

    def selectionSortAscending(self) -> None:
        list_size: int = self.values.size()

        for i in range(0, list_size - 1):
            min_index: int = i

            for j in range(i + 1, list_size):
                candidate: int = self.values.get(j)
                current_min: int = self.values.get(min_index)

                if candidate < current_min:
                    min_index = j

            if min_index != i:
                self.values.swap(i, min_index)