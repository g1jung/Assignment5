
from typing import List

def _sift_down(a: List[int], start: int, end: int) -> None:
    root = start
    while True:
        left = 2 * root + 1
        right = left + 1
        largest = root
        if left <= end and a[left] > a[largest]:
            largest = left
        if right <= end and a[right] > a[largest]:
            largest = right
        if largest == root:
            return
        a[root], a[largest] = a[largest], a[root]
        root = largest

def _build_max_heap(a: List[int]) -> None:
    for i in range((len(a) // 2) - 1, -1, -1):
        _sift_down(a, i, len(a) - 1)

def heapsort(a: List[int]) -> List[int]:
    n = len(a)
    if n <= 1:
        return a
    _build_max_heap(a)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        _sift_down(a, 0, end - 1)
    return a

def is_sorted(a: List[int]) -> bool:
    return all(a[i] <= a[i+1] for i in range(len(a)-1))
