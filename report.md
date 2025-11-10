
# Heaps, Heapsort, and Priority Queues — Implementation & Analysis

## Heapsort: Algorithm & Complexity
We use an array-backed max-heap. Building the heap bottom-up is O(n); extracting the maximum n times costs n·O(log n). Thus Heapsort runs in **O(n log n)** in the worst, average, and best cases and is **in-place (O(1) extra space)**.

## Priority Queue (Max-Heap)
- **Structure:** Python list implements the heap; `task_id→index` map supports O(log n) key updates.
- **Operations:** insert, extract_max, increase/decrease_key, is_empty.
- **Complexities:** All key ops are O(log n) (except is_empty: O(1)).

## Benchmarks
We compare Heapsort vs Randomized Quicksort vs Mergesort on random, sorted, and reversed arrays.
- Heapsort is consistently O(n log n) but can be slower due to less cache-friendly access.
- Randomized Quicksort often wins on average; remains robust on sorted/reversed.
- Mergesort is stable and predictable but uses O(n) extra space.

## Reproduce
```bash
python3 -m pip install -U matplotlib
python3 benchmark.py
python3 scheduler_sim.py
```
Artifacts: results.csv, plot_random.png, plot_sorted.png, plot_reversed.png.
