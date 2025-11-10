
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

@dataclass(order=True)
class Task:
    priority: int
    task_id: str
    arrival_time: float = 0.0
    deadline: Optional[float] = None
    payload: Any = None

class PriorityQueue:
    def __init__(self):
        self._heap: List[Task] = []
        self._pos: Dict[str, int] = {}

    def __len__(self) -> int:
        return len(self._heap)

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    def _swap(self, i: int, j: int):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
        self._pos[self._heap[i].task_id] = i
        self._pos[self._heap[j].task_id] = j

    def _sift_up(self, i: int):
        while i > 0:
            p = self._parent(i)
            if self._heap[p].priority >= self._heap[i].priority:
                break
            self._swap(i, p)
            i = p

    def _sift_down(self, i: int):
        n = len(self._heap)
        while True:
            l = self._left(i)
            r = self._right(i)
            largest = i
            if l < n and self._heap[l].priority > self._heap[largest].priority:
                largest = l
            if r < n and self._heap[r].priority > self._heap[largest].priority:
                largest = r
            if largest == i:
                break
            self._swap(i, largest)
            i = largest

    def insert(self, task: Task) -> None:
        if task.task_id in self._pos:
            raise ValueError("Task with this ID already present")
        self._heap.append(task)
        idx = len(self._heap) - 1
        self._pos[task.task_id] = idx
        self._sift_up(idx)

    def extract_max(self) -> Task:
        if not self._heap:
            raise IndexError("extract_max from empty queue")
        max_task = self._heap[0]
        last = self._heap.pop()
        del self._pos[max_task.task_id]
        if self._heap:
            self._heap[0] = last
            self._pos[last.task_id] = 0
            self._sift_down(0)
        return max_task

    def increase_key(self, task_id: str, new_priority: int) -> None:
        if task_id not in self._pos:
            raise KeyError("Task not found")
        i = self._pos[task_id]
        if new_priority < self._heap[i].priority:
            raise ValueError("New priority is lower; use decrease_key")
        self._heap[i].priority = new_priority
        self._sift_up(i)

    def decrease_key(self, task_id: str, new_priority: int) -> None:
        if task_id not in self._pos:
            raise KeyError("Task not found")
        i = self._pos[task_id]
        if new_priority > self._heap[i].priority:
            raise ValueError("New priority is higher; use increase_key")
        self._heap[i].priority = new_priority
        self._sift_down(i)
