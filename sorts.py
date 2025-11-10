
import random
from typing import List

def randomized_quicksort(a: List[int]) -> List[int]:
    def _qs(lo, hi):
        while lo < hi:
            p = random.randint(lo, hi)
            a[p], a[hi] = a[hi], a[p]
            pivot = a[hi]
            i = lo
            for j in range(lo, hi):
                if a[j] <= pivot:
                    a[i], a[j] = a[j], a[i]
                    i += 1
            a[i], a[hi] = a[hi], a[i]
            if i - 1 - lo < hi - (i + 1):
                if lo < i - 1:
                    _qs(lo, i - 1)
                lo = i + 1
            else:
                if i + 1 < hi:
                    _qs(i + 1, hi)
                hi = i - 1
    _qs(0, len(a)-1)
    return a

def mergesort(a: List[int]) -> List[int]:
    n = len(a)
    if n <= 1:
        return a
    mid = n // 2
    left = mergesort(a[:mid])
    right = mergesort(a[mid:])
    i = j = 0
    out = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:]); out.extend(right[j:])
    a[:] = out
    return a

def is_sorted(a: List[int]) -> bool:
    return all(a[i] <= a[i+1] for i in range(len(a)-1))
