# part_a.py
import numpy as np
import matplotlib.pyplot as plt
import csv
import time
from graph_utils import gen_matrix, count_edges_matrix
from dijkstra_matrix_arr import dijkstra_matrix

def run_a(n_values, runs=3, avg_deg=3):
    times_sparse_all_runs = []
    edge_sparse_all_runs = []

    times_dense_all_runs = []
    edge_dense_all_runs = []

    for run in range(runs):
        time_run = []
        edge_run = []
        for n in n_values:
            W_sparse = gen_matrix(n, p=min(1, avg_deg/(n-1)))
            edge_run.append(count_edges_matrix(W_sparse))
            start_time = time.time()
            d, pi, S = dijkstra_matrix(W_sparse, 0)
            end_time = time.time()
            time_run.append(end_time - start_time)
        times_sparse_all_runs.append(time_run)
        edge_sparse_all_runs.append(edge_run)

    for run in range(runs):
        time_run = []
        edge_run = []
        for n in n_values:
            W_dense = gen_matrix(n, p=0.8)
            edge_run.append(count_edges_matrix(W_dense))
            start_time = time.time()
            d, pi, S = dijkstra_matrix(W_dense, 0)
            end_time = time.time()
            time_run.append(end_time - start_time)
        times_dense_all_runs.append(time_run)
        edge_dense_all_runs.append(edge_run)

    return times_sparse_all_runs, edge_sparse_all_runs, times_dense_all_runs, edge_dense_all_runs

if __name__ == "__main__":
    n_values = list(range(2, 201))
    times_sparse, edges_sparse, times_dense, edges_dense = run_a(n_values)

    time_mean_sparse = np.mean(times_sparse, axis=0)
    time_mean_dense = np.mean(times_dense, axis=0)

    plt.figure(figsize=(8,5))
    plt.plot(n_values, time_mean_sparse, label="Sparse")
    plt.plot(n_values, time_mean_dense, label="Dense")
    plt.xlabel("Number of Vertices (V)")
    plt.ylabel("CPU Runtime (seconds)")
    plt.title("Part (a) — Runtime of Matrix+Array Implementation")
    plt.legend(); plt.grid(True); plt.show()
