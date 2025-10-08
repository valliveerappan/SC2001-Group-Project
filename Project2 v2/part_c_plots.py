# part_c.py
import numpy as np
import matplotlib.pyplot as plt
from part_a_plots import run_a
from part_b_plots import run_b

# Vertex sizes to test
n_values = list(range(2, 201))

# Run Part (a) experiments (Matrix + Array)
times_sparse_a, edges_sparse_a, times_dense_a, edges_dense_a = run_a(n_values)
time_mean_sparse_a = np.mean(times_sparse_a, axis=0)
time_mean_dense_a = np.mean(times_dense_a, axis=0)
edge_mean_sparse_a = np.mean(edges_sparse_a, axis=0)
edge_mean_dense_a = np.mean(edges_dense_a, axis=0)

# Run Part (b) experiments (List + Heap)
times_sparse_b, edges_sparse_b, times_dense_b, edges_dense_b = run_b(n_values)
time_mean_sparse_b = np.mean(times_sparse_b, axis=0)
time_mean_dense_b = np.mean(times_dense_b, axis=0)
edge_mean_sparse_b = np.mean(edges_sparse_b, axis=0)
edge_mean_dense_b = np.mean(edges_dense_b, axis=0)

# ---------------------------
# 1) Runtime: Sparse vs Dense, A vs B
# ---------------------------
plt.figure(figsize=(10,6))
plt.plot(n_values, time_mean_sparse_a, label="A Matrix+Array — Sparse")
plt.plot(n_values, time_mean_dense_a,  label="A Matrix+Array — Dense")
plt.plot(n_values, time_mean_sparse_b, label="B List+Heap — Sparse")
plt.plot(n_values, time_mean_dense_b,  label="B List+Heap — Dense")
plt.xlabel("Number of Vertices (V)")
plt.ylabel("Empirical Runtime (seconds)")
plt.title("Part (c) — Overall Runtime Comparison (A vs B)")
plt.legend(); plt.grid(True); plt.show()

# ---------------------------
# 2) Runtime: Dense only, A vs B
# ---------------------------
plt.figure(figsize=(10,6))
plt.plot(n_values, time_mean_dense_a, label="A Matrix+Array — Dense")
plt.plot(n_values, time_mean_dense_b, label="B List+Heap — Dense")
plt.xlabel("Number of Vertices (V)")
plt.ylabel("Empirical Runtime (seconds)")
plt.title("Part (c) — Dense Graph Runtime Comparison (A vs B)")
plt.legend(); plt.grid(True); plt.show()

# ---------------------------
# 3) Runtime: Sparse only, A vs B
# ---------------------------
plt.figure(figsize=(10,6))
plt.plot(n_values, time_mean_sparse_a, label="A Matrix+Array — Sparse")
plt.plot(n_values, time_mean_sparse_b, label="B List+Heap — Sparse")
plt.xlabel("Number of Vertices (V)")
plt.ylabel("Runtime (seconds)")
plt.title("Part (c) — Sparse Graph Runtime Comparison (A vs B)")
plt.legend(); plt.grid(True); plt.show()

# ---------------------------
# Optional: export CSV for Part C
# ---------------------------
import csv

output_file_c = "part_c_results.csv"
with open(output_file_c, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["GraphType", "|V|", "|E| (A)", "Time (A)", "|E| (B)", "Time (B)", "Speedup A/B"])

    for i, V in enumerate(n_values):
        # Sparse
        E_a_s = int(edge_mean_sparse_a[i])
        E_b_s = int(edge_mean_sparse_b[i])
        t_a_s = float(time_mean_sparse_a[i])
        t_b_s = float(time_mean_sparse_b[i])
        speedup_s = t_a_s / t_b_s if t_b_s > 0 else float('inf')
        writer.writerow(["Sparse", V, E_a_s, f"{t_a_s:.6f}", E_b_s, f"{t_b_s:.6f}", f"{speedup_s:.6f}"])

        # Dense
        E_a_d = int(edge_mean_dense_a[i])
        E_b_d = int(edge_mean_dense_b[i])
        t_a_d = float(time_mean_dense_a[i])
        t_b_d = float(time_mean_dense_b[i])
        speedup_d = t_a_d / t_b_d if t_b_d > 0 else float('inf')
        writer.writerow(["Dense", V, E_a_d, f"{t_a_d:.6f}", E_b_d, f"{t_b_d:.6f}", f"{speedup_d:.6f}"])

print(f"✅ Part C results saved to '{output_file_c}'")
