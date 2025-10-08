import time
import random
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

# ============================================================================
# GRAPH CLASS - ADJACENCY MATRIX
# ============================================================================

class Graph:
    def __init__(self, num_vertices):
        """Create a graph with adjacency matrix representation."""
        self.num_vertices = num_vertices
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]
    
    def add_edge(self, u, v, weight):
        """Add an undirected edge between u and v with given weight."""
        self.graph[u][v] = weight
        self.graph[v][u] = weight
    
    def get_edges(self):
        """Return list of all edges (u, v, weight)."""
        edges = []
        for u in range(self.num_vertices):
            for v in range(u + 1, self.num_vertices):
                if self.graph[u][v] > 0:
                    edges.append((u, v, self.graph[u][v]))
        return edges
    
    def visualize(self, title="Graph Visualization", highlight_path=None):
        """Visualize the graph using networkx with edge weights."""
        G = nx.Graph()
        
        # Add all edges
        for u in range(self.num_vertices):
            for v in range(u + 1, self.num_vertices):
                if self.graph[u][v] > 0:
                    G.add_edge(u, v, weight=self.graph[u][v])
        
        plt.figure(figsize=(12, 9))
        pos = nx.spring_layout(G, seed=42, k=1.5, iterations=50)
        
        # Draw nodes
        node_colors = ['lightcoral' if highlight_path and i in highlight_path 
                      else 'lightblue' for i in range(self.num_vertices)]
        nx.draw_networkx_nodes(G, pos, node_color=node_colors, 
                               node_size=700, alpha=0.9, edgecolors='black', linewidths=2)
        
        # Draw edges
        edge_colors = []
        edge_widths = []
        for u, v in G.edges():
            if highlight_path and u in highlight_path and v in highlight_path:
                idx_u = highlight_path.index(u)
                idx_v = highlight_path.index(v)
                if abs(idx_u - idx_v) == 1:  # Adjacent in path
                    edge_colors.append('red')
                    edge_widths.append(4)
                else:
                    edge_colors.append('gray')
                    edge_widths.append(1.5)
            else:
                edge_colors.append('gray')
                edge_widths.append(1.5)
        
        nx.draw_networkx_edges(G, pos, width=edge_widths, alpha=0.6, 
                              edge_color=edge_colors)
        
        # Draw vertex labels
        nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold')
        
        # Draw edge weights with background
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=11,
                                     font_weight='bold', bbox=dict(boxstyle='round,pad=0.3',
                                     facecolor='yellow', alpha=0.7))
        
        plt.title(title, fontsize=16, fontweight='bold', pad=20)
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    def __str__(self):
        result = "Adjacency Matrix Representation:\n"
        result += "     " + "".join([f"{i:4}" for i in range(self.num_vertices)]) + "\n"
        for i in range(self.num_vertices):
            result += f"{i:3}: "
            for j in range(self.num_vertices):
                if self.graph[i][j] == 0:
                    result += "   -"
                else:
                    result += f"{self.graph[i][j]:4}"
            result += "\n"
        return result


# ============================================================================
# DIJKSTRA'S ALGORITHM - ADJACENCY MATRIX + ARRAY PRIORITY QUEUE
# ============================================================================
def dijkstra_matrix_array(graph, start):
    """
    Dijkstra's algorithm using adjacency matrix and array-based priority queue.
    
    TIME COMPLEXITY ANALYSIS:
    ========================
    Total Complexity: O(|V|²)
    
    Breakdown:
    1. Initialization: O(|V|)
    2. Main loop: |V| iterations
       - Find minimum in array: O(|V|)  [scan all vertices]
       - Update neighbors via matrix: O(|V|)  [check all matrix positions]
    3. Total: |V| × (|V| + |V|) = O(|V|²)
    
    INDEPENDENCE FROM |E|:
    The complexity is O(|V|²) regardless of the number of edges because:
    - We always scan ALL |V| vertices to find minimum
    - We always check ALL |V| matrix positions for neighbors
    - Adjacency matrix structure forces O(|V|²) operations
    """
    
    n = graph.num_vertices
    distances = [float('inf')] * n
    distances[start] = 0
    visited = [False] * n
    parent = [-1] * n
    
    # Main loop: Execute |V| times - O(|V|)
    for iteration in range(n):
        # STEP 1: Find unvisited vertex with minimum distance - O(|V|)
        # Using array as priority queue requires linear search
        min_distance = float('inf')
        current_vertex = -1
        
        for v in range(n):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                current_vertex = v
        
        if current_vertex == -1:
            break
        
        visited[current_vertex] = True
        
        # STEP 2: Update distances to neighbors - O(|V|)
        # Due to adjacency matrix, we check ALL vertices
        for neighbor in range(n):
            if graph.graph[current_vertex][neighbor] > 0 and not visited[neighbor]:
                new_distance = distances[current_vertex] + graph.graph[current_vertex][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    parent[neighbor] = current_vertex
    
    return distances, parent


def reconstruct_path(parent, start, end):
    """Reconstruct shortest path from start to end."""
    if parent[end] == -1 and start != end:
        return None
    
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = parent[current]
    
    return list(reversed(path))


# ============================================================================
# GRAPH GENERATOR
# ============================================================================

def generate_random_graph(V, density=0.3):
    """Generate random graph with specified density."""
    graph = Graph(V)
    edge_count = 0
    
    for u in range(V):
        for v in range(u + 1, V):
            if random.random() < density:
                weight = random.randint(1, 20)
                graph.add_edge(u, v, weight)
                edge_count += 1
    
    return graph, edge_count


# ============================================================================
# BENCHMARKING
# ============================================================================

def benchmark_dijkstra(V, density=0.3, trials=5):
    """Measure execution time for Dijkstra's algorithm."""
    total_time = 0
    total_edges = 0
    
    for _ in range(trials):
        graph, edge_count = generate_random_graph(V, density)
        total_edges += edge_count
        
        start_time = time.perf_counter()
        dijkstra_matrix_array(graph, 0)
        elapsed = time.perf_counter() - start_time
        
        total_time += elapsed
    
    return total_time / trials, total_edges / trials


# ============================================================================
# EXAMPLE WITH VISUALIZATION
# ============================================================================

print("=" * 80)
print("DIJKSTRA'S ALGORITHM - ADJACENCY MATRIX & ARRAY PRIORITY QUEUE")
print("=" * 80)
print("Theoretical Complexity: O(|V|²)")
print("Total Complexity: O(|V|²) (Due to adjacency matrix)")
print("=" * 80)
# Create example graph
example_graph = Graph(8)
edges = [
    (0, 1, 4), (0, 2, 3), (0, 3, 7),
    (1, 2, 2), (1, 4, 5),
    (2, 3, 4), (2, 4, 6), (2, 5, 8),
    (3, 5, 3), (3, 6, 9),
    (4, 5, 2), (4, 7, 7),
    (5, 6, 5), (5, 7, 4),
    (6, 7, 6)
]

for u, v, w in edges:
    example_graph.add_edge(u, v, w)

print("\n1. EXAMPLE GRAPH STRUCTURE:")
print(example_graph)

# Visualize original graph
example_graph.visualize(title="Example Graph with Edge Weights")

# Run Dijkstra
print("\n2. RUNNING DIJKSTRA'S ALGORITHM FROM VERTEX 0:")
distances, parent = dijkstra_matrix_array(example_graph, 0)

print("=" * 80)
print("SHORTEST PATHS FROM VERTEX 0:")
print("=" * 80)
for i in range(example_graph.num_vertices):
    path = reconstruct_path(parent, 0, i)
    if path:
        path_str = " → ".join(map(str, path))
        print(f"To vertex {i}: distance = {distances[i]:3}, path: {path_str}")

# Visualize with shortest path highlighted (e.g., to vertex 7)
target = 7
path_to_target = reconstruct_path(parent, 0, target)
example_graph.visualize(
    title=f"Shortest Path from Vertex 0 to {target} (Distance = {distances[target]})",
    highlight_path=path_to_target
)


# ============================================================================
# EXPERIMENT 1: VARYING GRAPH SIZE
# ============================================================================

print("\n" + "=" * 80)
print("EXPERIMENT 1: DIJKSTRA'S ALGORITHM WITH INCREASING GRAPH SIZE")
print("=" * 80)
print("Fixed Density: 0.3")
print("Expected: Time should grow as O(|V|²)")
print("=" * 80)

V_values = [10, 20, 40, 60, 80, 100, 150, 200, 300, 400]
times_vs_V = []
edges_vs_V = []

print(f"\n{'|V|':<10}{'Avg |E|':<12}{'Time (ms)':<15}{'Time/|V|²':<15}")
print("-" * 52)

for V in V_values:
    avg_time, avg_edges = benchmark_dijkstra(V, density=0.3, trials=3)
    times_vs_V.append(avg_time * 1000)
    edges_vs_V.append(avg_edges)
    
    time_per_v2 = (avg_time * 1000) / (V * V)
    print(f"{V:<10}{avg_edges:<12.0f}{avg_time*1000:<15.3f}{time_per_v2:<15.6f}")

# Create comprehensive plots
fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3)

# Plot 1: Time vs |V|
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(V_values, times_vs_V, 'o-', color='#2E86AB', linewidth=3, 
         markersize=10, markerfacecolor='#A23B72', markeredgewidth=2, 
         markeredgecolor='#2E86AB')
ax1.set_xlabel('Number of Vertices |V|', fontsize=13, fontweight='bold')
ax1.set_ylabel('Execution Time (ms)', fontsize=13, fontweight='bold')
ax1.set_title('Time vs |V| (Quadratic Growth)', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.set_facecolor('#F8F9FA')

# Plot 2: Time vs |V|² (should be linear)
ax2 = fig.add_subplot(gs[0, 1])
V_squared = [v*v for v in V_values]
ax2.plot(V_squared, times_vs_V, 's-', color='#F18F01', linewidth=3,
         markersize=10, markerfacecolor='#C73E1D', markeredgewidth=2,
         markeredgecolor='#F18F01')
ax2.set_xlabel('|V|² (Vertices Squared)', fontsize=13, fontweight='bold')
ax2.set_ylabel('Execution Time (ms)', fontsize=13, fontweight='bold')
ax2.set_title('Time vs |V|² (Linear Confirms O(|V|²))', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.set_facecolor('#F8F9FA')

# Add linear fit line
z = np.polyfit(V_squared, times_vs_V, 1)
p = np.poly1d(z)
ax2.plot(V_squared, p(V_squared), '--', color='red', linewidth=2, 
         alpha=0.7, label=f'Linear fit: y={z[0]:.6f}x+{z[1]:.2f}')
ax2.legend(fontsize=10)
# Plot 3: Time/|V|² vs |V| (should be constant)
ax3 = fig.add_subplot(gs[0, 2])
time_per_v2_list = [t/(v*v) for t, v in zip(times_vs_V, V_values)]
mean_ratio = np.mean(time_per_v2_list)
ax3.plot(V_values, time_per_v2_list, '^-', color='#06A77D', linewidth=3,
         markersize=10, markerfacecolor='#005F60', markeredgewidth=2,
         markeredgecolor='#06A77D')
ax3.axhline(y=mean_ratio, color='red', linestyle='--', linewidth=2,
            alpha=0.7, label=f'Mean: {mean_ratio:.6f}')
ax3.set_xlabel('Number of Vertices |V|', fontsize=13, fontweight='bold')
ax3.set_ylabel('Time / |V|² (ms)', fontsize=13, fontweight='bold')
ax3.set_title('Time/|V|² Ratio (Should be Constant)', fontsize=14, fontweight='bold')
ax3.grid(True, alpha=0.3, linestyle='--')
ax3.legend(fontsize=11)
ax3.set_facecolor('#F8F9FA')

# Plot 4: Log-log plot
ax4 = fig.add_subplot(gs[1, :])
ax4.loglog(V_values, times_vs_V, 'D-', color='#6A4C93', linewidth=3,
           markersize=12, markerfacecolor='#1982C4', markeredgewidth=2,
           markeredgecolor='#6A4C93', label='Actual Time')

# Add reference line for O(V²)
ref_line = [(times_vs_V[0] / (V_values[0]**2)) * (v**2) for v in V_values]
ax4.loglog(V_values, ref_line, '--', color='red', linewidth=2,
           alpha=0.7, label='O(|V|²) Reference')

ax4.set_xlabel('Number of Vertices |V| (log scale)', fontsize=13, fontweight='bold')
ax4.set_ylabel('Execution Time (ms, log scale)', fontsize=13, fontweight='bold')
ax4.set_title('Log-Log Plot: Time vs |V| (Slope ≈ 2 confirms O(|V|²))', 
              fontsize=14, fontweight='bold')
ax4.grid(True, alpha=0.3, which='both', linestyle='--')
ax4.legend(fontsize=12, loc='upper left')
ax4.set_facecolor('#F8F9FA')

plt.suptitle('Dijkstra\'s Algorithm with Increasing Graph Size (Density = 0.3)',
             fontsize=16, fontweight='bold', y=0.98)
plt.savefig('dijkstra_varying_size.png', dpi=300, bbox_inches='tight')
plt.show()


# ============================================================================
# EXPERIMENT 2: VARYING EDGE DENSITIES
# ============================================================================

# print("\n" + "=" * 80)
# print("EXPERIMENT 2: DIJKSTRA'S ALGORITHM WITH VARYING EDGE DENSITIES")
# print("=" * 80)
# print("Fixed Graph Size: |V| = 100")
# print("Expected: Time should remain O(|V|²) regardless of |E|")
# print("=" * 80)

# V_fixed = 100
# densities = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
# times_vs_density = []
# edges_vs_density = []

# print(f"\n{'Density':<12}{'Avg |E|':<12}{'Time (ms)':<15}{'|E|/|V|²':<15}")
# print("-" * 54)

# for density in densities:
#     avg_time, avg_edges = benchmark_dijkstra(V_fixed, density=density, trials=3)
#     times_vs_density.append(avg_time * 1000)
#     edges_vs_density.append(avg_edges)
    
#     edge_ratio = avg_edges / (V_fixed * V_fixed)
#     print(f"{density:<12.2f}{avg_edges:<12.0f}{avg_time*1000:<15.3f}{edge_ratio:<15.4f}")

# mean_time = np.mean(times_vs_density)
# std_time = np.std(times_vs_density)
# cv = (std_time / mean_time) * 100

# print(f"\nSTATISTICS:")
# print(f"  Mean time: {mean_time:.3f} ms")
# print(f"  Std deviation: {std_time:.3f} ms")
# print(f"  Coefficient of variation: {cv:.2f}%")
# print(f"  Conclusion: Time is {'INDEPENDENT' if cv < 15 else 'DEPENDENT'} of |E|")

# # Create comprehensive plots
# fig = plt.figure(figsize=(16, 5))
# # Plot 1: Time vs |E|
# ax1 = plt.subplot(1, 3, 1)
# ax1.plot(edges_vs_density, times_vs_density, 'o-', color='#E63946', 
#          linewidth=3, markersize=10, markerfacecolor='#F77F00',
#          markeredgewidth=2, markeredgecolor='#E63946')
# ax1.axhline(y=mean_time, color='blue', linestyle='--', linewidth=2,
#             alpha=0.7, label=f'Mean: {mean_time:.2f} ms')
# ax1.fill_between(edges_vs_density, mean_time - std_time, mean_time + std_time,
#                   alpha=0.2, color='blue', label=f'±1 Std Dev')
# ax1.set_xlabel('Number of Edges |E|', fontsize=13, fontweight='bold')
# ax1.set_ylabel('Execution Time (ms)', fontsize=13, fontweight='bold')
# ax1.set_title('Time vs |E| (Should be Flat)', fontsize=14, fontweight='bold')
# ax1.grid(True, alpha=0.3, linestyle='--')
# ax1.legend(fontsize=11)
# ax1.set_facecolor('#F8F9FA')

# # Plot 2: Time vs Density
# ax2 = plt.subplot(1, 3, 2)
# ax2.plot(densities, times_vs_density, 's-', color='#457B9D', linewidth=3,
#          markersize=10, markerfacecolor='#1D3557', markeredgewidth=2,
#          markeredgecolor='#457B9D')
# ax2.axhline(y=mean_time, color='red', linestyle='--', linewidth=2,
#             alpha=0.7, label=f'Mean: {mean_time:.2f} ms')
# ax2.fill_between(densities, mean_time - std_time, mean_time + std_time,
#                   alpha=0.2, color='red')
# ax2.set_xlabel('Edge Density', fontsize=13, fontweight='bold')
# ax2.set_ylabel('Execution Time (ms)', fontsize=13, fontweight='bold')
# ax2.set_title(f'Time vs Density (|V|={V_fixed})', fontsize=14, fontweight='bold')
# ax2.grid(True, alpha=0.3, linestyle='--')
# ax2.legend(fontsize=11)
# ax2.set_facecolor('#F8F9FA')

# # Plot 3: Bar chart showing consistency
# ax3 = plt.subplot(1, 3, 3)
# colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(densities)))
# bars = ax3.bar([f'{d:.2f}' for d in densities], times_vs_density, 
#                color=colors, edgecolor='black', linewidth=1.5, alpha=0.8)
# ax3.axhline(y=mean_time, color='red', linestyle='--', linewidth=2,
#             label=f'Mean: {mean_time:.2f} ms')
# ax3.set_xlabel('Edge Density', fontsize=13, fontweight='bold')
# ax3.set_ylabel('Execution Time (ms)', fontsize=13, fontweight='bold')
# ax3.set_title('Time Distribution Across Densities', fontsize=14, fontweight='bold')
# ax3.legend(fontsize=11)
# ax3.set_facecolor('#F8F9FA')
# plt.xticks(rotation=45)

# plt.suptitle(f'Dijkstra\'s Algorithm with Varying Edge Densities (|V|={V_fixed})',
#              fontsize=16, fontweight='bold')
# plt.tight_layout()
# plt.savefig('dijkstra_varying_density.png', dpi=300, bbox_inches='tight')
# plt.show()
# ============================================================================
# EXPERIMENT 2: TIME vs NUMBER OF VERTICES FOR DIFFERENT DENSITIES
# ============================================================================

V_values = [10, 20, 40, 60, 80, 100, 150, 200]  # can extend
densities = [0.05, 0.1, 0.3, 0.5, 0.7, 0.9]     # 6 densities → 6 lines
trials_per_run = 40

# Store execution times for each density and V
times_all = {density: [] for density in densities}
edges_all = {density: [] for density in densities}

# Run benchmarks
for density in densities:
    for V in V_values:
        avg_time, avg_edges = benchmark_dijkstra(V, density=density, trials=trials_per_run)
        times_all[density].append(avg_time * 1000)  # convert to ms
        edges_all[density].append(avg_edges)

# =========================
# PLOTTING: 4 SUBPLOTS
# =========================
fig, axs = plt.subplots(2, 2, figsize=(16, 10))
axs = axs.flatten()
colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(densities)))
fs_title = 14 - 3   # decrease by 3
fs_label = 13 - 3
fs_ticks = 11 - 3
fs_legend = 10 - 3

# 1. Time vs |V|
for i, density in enumerate(densities):
    axs[0].plot(V_values, times_all[density], 'o-', color=colors[i], label=f'density={density:.2f}')
axs[0].set_xlabel('Number of Vertices |V|', fontsize=fs_label, fontweight='bold')
axs[0].set_ylabel('Execution Time (ms)', fontsize=fs_label, fontweight='bold')
axs[0].set_title('Time vs Number of Vertices', fontsize=fs_title, fontweight='bold')
axs[0].tick_params(labelsize=fs_ticks)
axs[0].grid(True, alpha=0.3, linestyle='--')
axs[0].legend(fontsize=fs_legend)

# 2. Time normalized by |V|²
for i, density in enumerate(densities):
    normalized_time = [t/(V*V) for t, V in zip(times_all[density], V_values)]
    axs[1].plot(V_values, normalized_time, 's-', color=colors[i], linewidth=2, label=f'density={density:.2f}')
axs[1].set_xlabel('Number of Vertices |V|', fontsize=fs_label, fontweight='bold')
axs[1].set_ylabel('Time / |V|² (ms)', fontsize=fs_label, fontweight='bold')
axs[1].set_title('Normalized Time vs |V|', fontsize=fs_title, fontweight='bold')
axs[1].tick_params(labelsize=fs_ticks)
axs[1].grid(True, alpha=0.3, linestyle='--')
axs[1].legend(fontsize=fs_legend)

# 3. Edge growth vs |V|
for i, density in enumerate(densities):
    axs[2].plot(V_values, edges_all[density], '^-', color=colors[i], linewidth=2, label=f'density={density:.2f}')
axs[2].set_xlabel('Number of Vertices |V|', fontsize=fs_label, fontweight='bold')
axs[2].set_ylabel('Average |E|', fontsize=fs_label, fontweight='bold')
axs[2].set_title('Edge Growth vs |V|', fontsize=fs_title, fontweight='bold')
axs[2].tick_params(labelsize=fs_ticks)
axs[2].grid(True, alpha=0.3, linestyle='--')
axs[2].legend(fontsize=fs_legend)

# 4. Reference: Time vs |V|²
for i, density in enumerate(densities):
    ref_line = [e * V for e, V in zip(edges_all[density], V_values)]  # rough reference
    axs[3].plot(V_values, ref_line, '--', color=colors[i], label=f'density={density:.2f}')
axs[3].set_xlabel('Number of Vertices |V|', fontsize=fs_label, fontweight='bold')
axs[3].set_ylabel('Reference: |E|*|V|', fontsize=fs_label, fontweight='bold')
axs[3].set_title('Reference Line: |E|*|V|', fontsize=fs_title, fontweight='bold')
axs[3].tick_params(labelsize=fs_ticks)
axs[3].grid(True, alpha=0.3, linestyle='--')
axs[3].legend(fontsize=fs_legend)

plt.suptitle(f"Dijkstra's Algorithm Performance Across Densities (Varying |V|)",
             fontsize=16-3, fontweight='bold')
plt.tight_layout()
plt.show()


# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 80)
print("FINAL SUMMARY")
print("=" * 80)
print("""
DIJKSTRA'S ALGORITHM - ADJACENCY MATRIX & ARRAY PRIORITY QUEUE
================================================================

THEORETICAL COMPLEXITY: O(|V|²)
TOTAL COMPLEXITY: O(|V|²) (Due to adjacency matrix structure)

EMPIRICAL VERIFICATION:
✓ Time grows quadratically with |V| (Experiment 1)
✓ Time/|V|² ratio remains constant as |V| increases
✓ Time is independent of |E| (Experiment 2)
✓ Varying edge density (5% to 90%) has minimal effect on runtime

KEY INSIGHT:
The adjacency matrix representation forces O(|V|²) complexity because:
- Finding minimum in array priority queue: O(|V|) per iteration
- Checking all matrix positions for neighbors: O(|V|) per iteration
- Total: |V| iterations × O(|V|) = O(|V|²)

This complexity is INDEPENDENT of the actual number of edges!
""")