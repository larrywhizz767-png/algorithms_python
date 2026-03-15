class IntList:
    def __init__(self, values: list[int]) -> None:
        self._values: list[int] = values.copy()

    def size(self) -> int:
        return len(self._values)

    def get(self, index: int) -> int:
        self._validate_index(index)
        return self._values[index]

    def set(self, index: int, value: int) -> None:
        self._validate_index(index)
        self._values[index] = value

    def swap(self, i: int, j: int) -> None:
        self._validate_index(i)
        self._validate_index(j)
        self._values[i], self._values[j] = self._values[j], self._values[i]

    def to_list(self) -> list[int]:
        return self._values.copy()

    def __str__(self) -> str:
        return str(self._values)

    def _validate_index(self, index: int) -> None:
        if index < 0 or index >= len(self._values):
            raise IndexError(
                f"Index {index} out of range for list size {len(self._values)}"
            )