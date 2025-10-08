# part_b.py
import numpy as np
import matplotlib.pyplot as plt
import csv
import time
import math
from graph_utils import gen_graph_connected
from dijkstra_list_heap import dijkstra_list_heap

def run_b(n_values, runs=3, avg_deg_sparse=3, avg_deg_dense_factor=0.5):
    times_sparse_all_runs = []
    edges_sparse_all_runs = []

    times_dense_all_runs = []
    edges_dense_all_runs = []

    for run in range(runs):
        time_run = []
        edge_run = []
        for n in n_values:
            adj_list_sparse, edge_sparse = gen_graph_connected(n, seed=1000+run*100+n, avg_deg=avg_deg_sparse)
            start_time = time.time()
            d, pi, S = dijkstra_list_heap(adj_list_sparse, start=1)
            end_time = time.time()
            time_run.append(end_time - start_time)
            edge_run.append(edge_sparse)
        times_sparse_all_runs.append(time_run)
        edges_sparse_all_runs.append(edge_run)

    for run in range(runs):
        time_run = []
        edge_run = []
        for n in n_values:
            avg_deg_dense = max(1, int(n * avg_deg_dense_factor))
            adj_list_dense, edge_dense = gen_graph_connected(n, seed=2000+run*100+n, avg_deg=avg_deg_dense)
            start_time = time.time()
            d, pi, S = dijkstra_list_heap(adj_list_dense, start=1)
            end_time = time.time()
            time_run.append(end_time - start_time)
            edge_run.append(edge_dense)
        times_dense_all_runs.append(time_run)
        edges_dense_all_runs.append(edge_run)

    return times_sparse_all_runs, edges_sparse_all_runs, times_dense_all_runs, edges_dense_all_runs

# Example usage
if __name__ == "__main__":
    n_values = list(range(2, 201))
    times_sparse, edges_sparse, times_dense, edges_dense = run_b(n_values)

    time_mean_sparse = np.mean(times_sparse, axis=0)
    time_mean_dense = np.mean(times_dense, axis=0)

    plt.figure(figsize=(8,5))
    plt.plot(n_values, time_mean_sparse, label="Sparse")
    plt.plot(n_values, time_mean_dense, label="Dense")
    plt.xlabel("Number of Vertices (V)")
    plt.ylabel("CPU Runtime (seconds)")
    plt.title("Part (b) — Runtime of List+Heap Implementation")
    plt.legend(); plt.grid(True); plt.show()
