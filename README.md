# Python Heap

## Explanation

A Heap is a specialized tree-based data structure that satisfies the heap property.

A **Min Heap** is a heap where the smallest element is always at the root.

Python provides the `heapq` module to implement a Min Heap efficiently.

## Problem Statement

Write a Python program to implement a Min Heap using Python's `heapq` module.

The program should support:

* Insertion
* Finding the minimum element
* Removing the minimum element
* Displaying the heap

## Features

* Implements a Min Heap
* Uses Python's built-in `heapq` module
* Supports insertion
* Supports minimum element retrieval
* Supports deletion of the minimum element
* Displays the heap

## How It Works

1. An empty list is created as the heap.
2. `heappush()` inserts elements while maintaining the heap property.
3. `heap[0]` gives the minimum element.
4. `heappop()` removes the minimum element.
5. The heap is displayed after operations.

## Technologies Used

* Python 3
* `heapq` module

## Data Structure Used

* Min Heap
* List

## Methods Used

* `heapq.heappush()`
* `heapq.heappop()`
* `heapq.heapify()`

## Program Flow

1. Create an empty heap.
2. Read elements from the user.
3. Insert elements into the heap.
4. Display the heap.
5. Display the minimum element.
6. Remove the minimum element.
7. Display the updated heap.

## Sample Input

```text id="u5o9qs"
Enter the number of elements: 5
Enter element 1: 40
Enter element 2: 10
Enter element 3: 30
Enter element 4: 20
Enter element 5: 50
```

## Sample Output

```text id="o2j5zy"
Min Heap: [10, 20, 30, 40, 50]
Minimum Element: 10
Removed Element: 10
Heap After Removal: [20, 40, 30, 50]
```

## Time Complexity

* Insertion: O(log n)
* Find Minimum: O(1)
* Delete Minimum: O(log n)

## Space Complexity

* O(n)

## Key Learning

* Understanding heaps
* Understanding Min Heap
* Learning heap operations
* Using the `heapq` module
* Understanding heap complexity

## File Location

```text id="w4h7qz"
Python-Heap/heap.py
```

## Repository Structure

```text id="t9e4mx"
Python-Heap/
│
├── heap.py
└── README.md
```

## Author

V.Harini
