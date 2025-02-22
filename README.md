# MSCS 532: Algorithms and Data Structures

## Shrisan Kapali

**Student ID:** 005032249

### Final Project Part 1 - Optimization in High-Performance Computing

### Installation and Execution

To run the program, execute the following commands in the terminal:

#### Installing Dependencies

```sh
py -m pip install sortedcontainers
py -m pip install matplotlib
```

#### Running the Program

```sh
py MSCS_532_Final_Project.py
```

---

## Final Report

An extensive dataset of size **10,000,000** was used to simulate and analyze High-Performance Computing (HPC) optimization techniques. Several search algorithms were implemented to evaluate their time complexity:

- **Linear Search**: O(n)
- **Binary Search**: O(log n)
- **Hash Table Search**: O(1)
- **B-Tree Search**: O(log n)
- **Quicksort**: O(n log n)

#### Key Implementations:

- The **Python `bisect` module** was used for binary search operations similar to B-Trees, where data is inserted in sorted order.
- An **LRU Cache** was implemented to enhance performance efficiency.
- **Threading** was introduced to parallelize search operations and assess performance improvements.
- **Stress testing** was conducted with varying dataset sizes to evaluate search performance for:
  - **Minimum and maximum values**
  - **Random values**
  - **Non-existent values**

> **Note:** If a search value does not exist in the dataset, the search function returns `-1` or `False`.

---

## Code Walkthrough

- **The total execution time of the project is approximately 1 minute**, but this may vary depending on system specifications.
- The execution time of each search algorithm was recorded and analyzed.
- The search index for each algorithm was printed.
- A **graphical analysis** of the time complexity for searching a random target was generated.

---

## Test Cases

- A **random target value** was selected, and all search algorithms were tested against it.
- Execution times were recorded and compared.

## Stress Testing

Stress tests were performed using dataset sizes of **100,000**, **300,000**, and **900,000**. The target values included:

- **Maximum value**
- **Minimum value**
- **Random value**
- **Non-existent value**

The results were visualized in graphical format.

---

## Project Files on GitHub

- **Python Program**: `MSCS_532_Final_Project.py`
- **Final Report**: `MSCS_532_Final_Project_1.pdf`
- **Graph Screenshots**: Images showcasing search result graphs.

---
