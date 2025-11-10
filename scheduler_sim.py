
import random
from dataclasses import dataclass
from typing import List
from priority_queue import PriorityQueue, Task

@dataclass
class Result:
    schedule: List[str]
    late_count: int
    avg_completion_index: float

def simulate(num_tasks=20, seed=0) -> Result:
    random.seed(seed)
    pq = PriorityQueue()
    t = 0
    for i in range(num_tasks):
        pr = random.randint(1, 100)
        deadline = t + random.randint(1, 10)
        task = Task(priority=pr, task_id=f"T{i}", arrival_time=t, deadline=deadline)
        pq.insert(task)
        if i % 5 == 0:
            pq.increase_key(task.task_id, task.priority + random.randint(0, 10))
        t += random.randint(0, 2)
    schedule = []
    time_index = 0
    late = 0
    while not pq.is_empty():
        current = pq.extract_max()
        schedule.append(current.task_id)
        if current.deadline is not None and time_index > current.deadline:
            late += 1
        time_index += 1
    avg_index = sum(range(len(schedule))) / max(1, len(schedule))
    return Result(schedule=schedule, late_count=late, avg_completion_index=avg_index)

if __name__ == "__main__":
    r = simulate()
    print("Schedule:", r.schedule)
    print("Late tasks:", r.late_count, "Avg index:", r.avg_completion_index)
