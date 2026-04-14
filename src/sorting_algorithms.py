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

    def insertionSortAscending(self) -> None:
        list_size: int = self.values.size()
        for i in range(1, list_size):
            value_to_insert = self.values.get(i)
            scan_index = i - 1

            while scan_index >= 0 and self.values.get(scan_index) > value_to_insert:
                self.values.set(scan_index+1, self.values.get(scan_index))
                scan_index -= 1

            self.values.set(scan_index+1, value_to_insert)
    
    def cocktailSortAscending(self) -> None:
        list_size = self.values.size()
        didSwap = True

        while didSwap:
            didSwap = False

            
            for i in range(0, list_size - 1):
                if self.values.get(i) > self.values.get(i + 1):
                    self.values.swap(i, i + 1)
                    didSwap = True

            if not didSwap:
                break

            didSwap = False

            
            for i in range(list_size - 2, -1, -1):
                if self.values.get(i) > self.values.get(i + 1):
                    self.values.swap(i, i + 1)
                    didSwap = True
            

    def bubbleSortDescending(self) -> None:
        list_size: int = self.values.size()
        didSwap: bool = True

        while didSwap:
            didSwap = False

            for i in range(0, list_size - 1):
                current: int = self.values.get(i)
                next_value: int = self.values.get(i + 1)

                if current < next_value:  #
                    self.values.swap(i, i + 1)
                    didSwap = True

    def selectionSortDescending(self) -> None:
        list_size: int = self.values.size()

        for i in range(0, list_size - 1):
            max_index: int = i  

            for j in range(i + 1, list_size):
                candidate: int = self.values.get(j)
                current_max: int = self.values.get(max_index)

                if candidate > current_max:  
                    max_index = j

            if max_index != i:
                self.values.swap(i, max_index)

    def insertionSortDescending(self) -> None:
        list_size: int = self.values.size()
        for i in range(1, list_size):
            value_to_insert = self.values.get(i)
            scan_index = i - 1

            while scan_index >= 0 and self.values.get(scan_index) < value_to_insert:  
                self.values.set(scan_index + 1, self.values.get(scan_index))
                scan_index -= 1

            self.values.set(scan_index + 1, value_to_insert)

    def cocktailSortDescending(self) -> None:
        list_size = self.values.size()
        didSwap = True

        while didSwap:
            didSwap = False

            #forward pass
            for i in range(0, list_size - 1):
                if self.values.get(i) < self.values.get(i + 1):  
                    self.values.swap(i, i + 1)
                    didSwap = True

            if not didSwap:
                break

            didSwap = False

            #backward pass
            for i in range(list_size - 2, -1, -1):
                if self.values.get(i) < self.values.get(i + 1):  
                    self.values.swap(i, i + 1)
                    didSwap = True