# Algorithms in Python
![C++ compliant](https://img.shields.io/badge/C%2B%2B-compliant-295FFF?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Personal project](https://img.shields.io/badge/Project-personal-FF7437?style=for-the-badge&logo=sourcegraph&logoColor=white)

> My own exploration of (sorting) algorithms in Python


## <a id="about-the-project"></a><img src="assets/readme/icons/lucide/workflow.svg" width="28" alt="" /> About The Project

`algorithms_python` showcases my own exploration of algorithmic thinking in Python.

I’m using this space to work through classic sorting algorithms in a way that stays readable and easy to follow.

At the moment the repo is small and focused, but that is part of the point: it is a personal place to build intuition
step by step.

## <a id="implemented-algorithms"></a><img src="assets/readme/icons/lucide/circle-check-big.svg" width="28" alt="" /> Implemented Algorithms

| Algorithm      | Functions                                           | Idea                                                           |
|----------------|-----------------------------------------------------|----------------------------------------------------------------|
| Bubble Sort    | `bubbleSortAscending`, `bubbleSortDescending`       | Repeatedly swaps adjacent values until the list is ordered.    |
| Selection Sort | `selectionSortAscending`, `selectionSortDescending` | Selects the smallest remaining value and places it next.       |
| Inserton Sort  | `insertionSortAscending`, `insertionSortDescending` | 
| 

## <a id="installation"></a><img src="assets/readme/icons/lucide/terminal.svg" width="28" alt="" /> Installation

To clone the project:

```bash
git clone git@github.com:larrywhizz767-png/algorithms_python.git
```

## <a id="quick-start"></a><img src="assets/readme/icons/lucide/terminal.svg" width="28" alt="" /> Quick Start

The fastest way to try the project is to compile the small demo included in the repo:

```bash
uv run  algorithms_python
```

Expected output:

```text
1 3 4 7 9
```



## <a id="roadmap"></a><img src="assets/readme/icons/lucide/compass.svg" width="28" alt="" /> Roadmap

- add `mergeSortAscending` and `quickSortAscending`
- expand the repo with searching algorithms such as linear search and binary search
- add graph algorithms such as Dijkstra
- attach example inputs and outputs for each algorithm  