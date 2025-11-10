
import random, time, csv
from pathlib import Path
import matplotlib.pyplot as plt

from heapsort import heapsort, is_sorted as is_sorted_heap
from sorts import randomized_quicksort, mergesort, is_sorted as is_sorted_other

def gen_array(n, mode):
    if mode == "random":
        return [random.randint(0, 10**6) for _ in range(n)]
    elif mode == "sorted":
        return list(range(n))
    elif mode == "reversed":
        return list(range(n, 0, -1))
    else:
        raise ValueError("mode")

def time_one(fn, arr):
    a = list(arr)
    t0 = time.perf_counter()
    fn(a)
    dt = time.perf_counter() - t0
    check = is_sorted_heap(a) if fn is heapsort else is_sorted_other(a)
    assert check, "Array not sorted"
    return dt

def run(outdir: Path, sizes=(2000, 6000, 20000), modes=("random","sorted","reversed"), trials=3):
    rows = []
    algos = [
        ("heapsort", heapsort),
        ("quicksort_rand", randomized_quicksort),
        ("mergesort", mergesort),
    ]
    for n in sizes:
        for mode in modes:
            base_arr = gen_array(n, mode)
            for name, fn in algos:
                times = [time_one(fn, base_arr) for _ in range(trials)]
                avg = sum(times) / len(times)
                rows.append([name, mode, n, avg])
                print(f"{name:14s} {mode:8s} n={n:6d} avg={avg:.6f}s")
    out_csv = outdir / "results.csv"
    with out_csv.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["algo","mode","n","avg_seconds"])
        w.writerows(rows)
    for mode in modes:
        xs = []
        yh, yq, ym = [], [], []
        for n in sizes:
            xs.append(n)
            for name in ("heapsort","quicksort_rand","mergesort"):
                for r in rows:
                    if r[0]==name and r[1]==mode and r[2]==n:
                        if name=="heapsort": yh.append(r[3])
                        elif name=="quicksort_rand": yq.append(r[3])
                        else: ym.append(r[3])
        plt.figure()
        plt.plot(xs, yh, marker="o", label="Heapsort")
        plt.plot(xs, yq, marker="o", label="Randomized Quicksort")
        plt.plot(xs, ym, marker="o", label="Mergesort")
        plt.xlabel("n")
        plt.ylabel("Average runtime (s)")
        plt.title(f"Runtime vs n ({mode})")
        plt.legend()
        plt.tight_layout()
        plt.savefig(outdir / f"plot_{mode}.png", dpi=160)
        plt.close()
    print("Saved:", ", ".join([f"plot_{m}.png" for m in modes]))
    return rows

if __name__ == "__main__":
    out = Path(".")
    run(out)
