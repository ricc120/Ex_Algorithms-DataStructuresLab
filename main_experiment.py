import time
import csv
import random
from linked_list import DisjointSetLinkedList
from linked_list_weighted import DisjointSetLinkedListWeighted
from path_compression_forest import DisjointSetForest
from connected_components import connected_components

def generate_random_undirected_graph(n_nodes, n_edges):
    edges = set()
    while len(edges) < n_edges:
        u = random.randint(0, n_nodes - 1)
        v = random.randint(0, n_nodes - 1)
        if u != v:
            edges.add((min(u, v), max(u, v)))
    return list(edges)

def benchmark_single_run(n_nodes, n_edges, disjoint_set_class):
    edges = generate_random_undirected_graph(n_nodes, n_edges)
    start = time.perf_counter()
    connected_components(n_nodes, edges, disjoint_set_class)
    end = time.perf_counter()
    return end - start

def benchmark_all_structures():
    sizes = [100, 500, 1000, 2000, 3000]
    density = 2
    repetitions = 100

    results = []

    for size in sizes:
        n_edges = size * density
        for disjointSetClass in [DisjointSetLinkedList, DisjointSetLinkedListWeighted, DisjointSetForest]:
            times = []
            for _ in range(repetitions):
                t = benchmark_single_run(size, n_edges, disjointSetClass)
                times.append(t)
            avg_time = sum(times) / repetitions
            results.append({
                "n_nodes": size,
                "n_edges": n_edges,
                "structure": disjointSetClass.__name__,
                "avg_time_sec": round(avg_time, 6)
            })
    return results

def save_results(results, filename="benchmark_results.csv"):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

if __name__ == "__main__":
    results = benchmark_all_structures()
    save_results(results)
    print("Benchmark completed. Results saved to 'benchmark_results.csv'")
