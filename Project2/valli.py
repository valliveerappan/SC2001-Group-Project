import time
import random
import heapq
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx 

# ============================================================================
# GRAPH CLASS - ADJACENCY LIST
# ============================================================================

class GraphList:
    def __init__(self, num_vertices):
        """Create a graph with adjacency list representation."""
        self.num_vertices = num_vertices
        self.graph = [[] for _ in range(num_vertices)]
    
    def add_edge(self, u, v, weight):
        """Add an undirected edge between u and v with given weight."""
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
    
    def get_edges(self):
        """Return list of all edges (u, v, weight)."""
        edges = []
        seen = set()
        for u in range(self.num_vertices):
            for v, w in self.graph[u]:
                if (v, u) not in seen:
                    edges.append((u, v, w))
                    seen.add((u, v))
        return edges
    
    def visualize(self, title="Graph Visualization", highlight_path=None):
        """Visualize the graph using networkx with edge weights."""
        G = nx.Graph()
        
        # Add edges
        for u in range(self.num_vertices):
            for v, w in self.graph[u]:
                G.add_edge(u, v, weight=w)
        
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
                if abs(idx_u - idx_v) == 1:
                    edge_colors.append('red')
                    edge_widths.append(4)
                else:
                    edge_colors.append('gray')
                    edge_widths.append(1.5)
            else:
                edge_colors.append('gray')
                edge_widths.append(1.5)
        
        nx.draw_networkx_edges(G, pos, width=edge_widths, alpha=0.6, edge_color=edge_colors)
        nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold')
        
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=11, font_weight='bold',
                                     bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))
        
        plt.title(title, fontsize=16, fontweight='bold', pad=20)
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    def __str__(self):
        result = "Adjacency List Representation:\n"
        for u in range(self.num_vertices):
            neighbors = ", ".join(f"({v}, {w})" for v, w in self.graph[u])
            result += f"{u:3}: {neighbors}\n"
        return result


# ============================================================================
# DIJKSTRA'S ALGORITHM - ADJACENCY LIST + MIN-HEAP PRIORITY QUEUE
# ============================================================================
def dijkstra_list_heap(graph, start):
    """
    Dijkstra's algorithm using adjacency list and min-heap priority queue.
    
    TIME COMPLEXITY ANALYSIS:
    ========================
    Total Complexity: O((|V| + |E|) log |V|)
    
    Breakdown:
    1. Each vertex is extracted once → O(|V| log |V|)
    2. Each edge relaxation → O(|E| log |V|)
    3. Total: O((|V| + |E|) log |V|)
    
    DEPENDENCE ON |E|:
    Runtime increases with |E| since more edges mean more relaxations.
    Efficient for sparse graphs (|E| ≈ |V|).
    """
    n = graph.num_vertices
    distances = [float('inf')] * n
    parent = [-1] * n
    distances[start] = 0
    
    pq = [(0, start)]
    visited = [False] * n
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if visited[u]:
            continue
        visited[u] = True
        
        for v, weight in graph.graph[u]:
            if not visited[v] and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                parent[v] = u
                heapq.heappush(pq, (distances[v], v))
    
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

def generate_random_graph_list(V, density):
    """Generate random undirected graph with given density."""
    graph = GraphList(V)
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

def benchmark_dijkstra_list(V, density, trials=5):
    """Measure average execution time for Dijkstra's algorithm."""
    total_time = 0
    total_edges = 0
    
    for _ in range(trials):
        graph, edge_count = generate_random_graph_list(V, density)
        total_edges += edge_count
        
        start_time = time.perf_counter()
        dijkstra_list_heap(graph, 0)
        elapsed = time.perf_counter() - start_time
        total_time += elapsed
    
    return total_time / trials, total_edges / trials


# ============================================================================
# EXAMPLE WITH VISUALIZATION
# ============================================================================

print("=" * 80)
print("DIJKSTRA'S ALGORITHM - ADJACENCY LIST & MIN-HEAP PRIORITY QUEUE")
print("=" * 80)
print("Theoretical Complexity: O((|V| + |E|) log |V|)")
print("=" * 80)

example_graph = GraphList(8)
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
example_graph.visualize(title="Example Graph with Edge Weights")

print("\n2. RUNNING DIJKSTRA'S ALGORITHM FROM VERTEX 0:")
distances, parent = dijkstra_list_heap(example_graph, 0)

print("=" * 80)
print("SHORTEST PATHS FROM VERTEX 0:")
print("=" * 80)
for i in range(example_graph.num_vertices):
    path = reconstruct_path(parent, 0, i)
    if path:
        path_str = " → ".join(map(str, path))
        print(f"To vertex {i}: distance = {distances[i]:3}, path: {path_str}")
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
print("Expected: Time grows as O((|V| + |E|) log |V|)")
print("=" * 80)

V_values = [10, 20, 40, 60, 80, 100, 150, 200, 300, 400]
times_vs_V = []
edges_vs_V = []

print(f"\n{'|V|':<10}{'Avg |E|':<12}{'Time (ms)':<15}{'Time/log|V|':<15}")
print("-" * 52)


for V in V_values:
    avg_time, avg_edges = benchmark_dijkstra_list(V, density=0.3, trials=3)
    times_vs_V.append(avg_time * 1000)
    edges_vs_V.append(avg_edges)
    
    time_per_logv = (avg_time * 1000) / np.log2(V)
    print(f"{V:<10}{avg_edges:<12.0f}{avg_time*1000:<15.3f}{time_per_logv:<15.6f}")

fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3)

ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(V_values, times_vs_V, 'o-', color='#2E86AB', linewidth=3,
         markersize=10, markerfacecolor='#A23B72', markeredgewidth=2)
ax1.set_xlabel('Number of Vertices |V|', fontsize=12, fontweight='bold')
ax1.set_ylabel('Execution Time (ms)', fontsize=12, fontweight='bold')
ax1.set_title('Time vs |V| (Near Linear-Log Growth)', fontsize=10, fontweight='bold')
ax1.grid(True, alpha=0.3, linestyle='--')

ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(V_values, [t / np.log2(v) for t, v in zip(times_vs_V, V_values)],
         's-', color='#F18F01', linewidth=3, markersize=10,
         markerfacecolor='#C73E1D', markeredgewidth=2)
ax2.set_xlabel('|V|', fontsize=10, fontweight='bold')
ax2.set_ylabel('Time / log|V| (ms)', fontsize=10, fontweight='bold')
ax2.set_title('Normalized by log|V| (Approx Constant)', fontsize=10, fontweight='bold')
ax2.grid(True, alpha=0.3, linestyle='--')

ax3 = fig.add_subplot(gs[0, 2])
ax3.plot(V_values, edges_vs_V, '^-', color='#06A77D', linewidth=3,
         markersize=10, markerfacecolor='#005F60', markeredgewidth=2)
ax3.set_xlabel('Number of Vertices |V|', fontsize=10, fontweight='bold')
ax3.set_ylabel('Average |E|', fontsize=10, fontweight='bold')
ax3.set_title('Edge Growth vs |V| (Density = 0.3)', fontsize=10, fontweight='bold')
ax3.grid(True, alpha=0.3, linestyle='--')

ax4 = fig.add_subplot(gs[1, :])
ax4.loglog(V_values, times_vs_V, 'D-', color='#6A4C93', linewidth=3,
           markersize=12, markerfacecolor='#1982C4', markeredgewidth=2,
           label='Actual Time')
ref_line = [(times_vs_V[0] / ((V_values[0]) * np.log2(V_values[0]))) * (v * np.log2(v))
            for v in V_values]
ax4.loglog(V_values, ref_line, '--', color='red', linewidth=2, alpha=0.7, label='O(|V| log |V|) Ref')
ax4.set_xlabel('Number of Vertices |V| (log scale)', fontsize=12, fontweight='bold')
ax4.set_ylabel('Execution Time (ms, log scale)', fontsize=12, fontweight='bold')
ax4.set_title('Log-Log Plot: Time vs |V| (Slope ≈ log|V|)', fontsize=13, fontweight='bold')
ax4.grid(True, alpha=0.3, which='both', linestyle='--')
ax4.legend(fontsize=11)
plt.suptitle("Dijkstra's Algorithm with Increasing Graph Size (Adjacency List + Heap)",
             fontsize=15, fontweight='bold', y=0.98)
plt.savefig('dijkstra_list_varying_size.png', dpi=300, bbox_inches='tight')
plt.show()


# ============================================================================
# EXPERIMENT 2: VARYING EDGE DENSITIES
# ============================================================================

# print("\n" + "=" * 80)
# print("EXPERIMENT 2: DIJKSTRA'S ALGORITHM WITH VARYING EDGE DENSITIES")
# print("=" * 80)
# print("Fixed Graph Size: |V| = 100")
# print("Expected: Time increases with |E| since more relaxations occur")
# print("=" * 80)
# V_fixed = 100
# densities = [0.05, 0.1, 0.3, 0.5, 0.7, 0.9]
# times_vs_density = []
# edges_vs_density = []

# print(f"\n{'Density':<12}{'Avg |E|':<12}{'Time (ms)':<15}{'|E| log|V|':<15}")
# print("-" * 54)

# for density in densities:
#     avg_time, avg_edges = benchmark_dijkstra_list(V_fixed, density=density, trials=3)
#     times_vs_density.append(avg_time * 1000)
#     edges_vs_density.append(avg_edges)
#     print(f"{density:<12.2f}{avg_edges:<12.0f}{avg_time*1000:<15.3f}{avg_edges*np.log2(V_fixed):<15.3f}")

# fig = plt.figure(figsize=(16, 5))
# ax1 = plt.subplot(1, 3, 1)
# ax1.plot(edges_vs_density, times_vs_density, 'o-', color='#E63946',
#          linewidth=3, markersize=10, markerfacecolor='#F77F00', markeredgewidth=2)
# ax1.set_xlabel('Number of Edges |E|', fontsize=13, fontweight='bold')
# ax1.set_ylabel('Execution Time (ms)', fontsize=13, fontweight='bold')
# ax1.set_title('Time vs |E| (Should Rise)', fontsize=14, fontweight='bold')
# ax1.grid(True, alpha=0.3, linestyle='--')

# ax2 = plt.subplot(1, 3, 2)
# ax2.plot(densities, times_vs_density, 's-', color='#457B9D', linewidth=3,
#          markersize=10, markerfacecolor='#1D3557', markeredgewidth=2)
# ax2.set_xlabel('Edge Density', fontsize=13, fontweight='bold')
# ax2.set_ylabel('Execution Time (ms)', fontsize=13, fontweight='bold')
# ax2.set_title(f'Time vs Density (|V|={V_fixed})', fontsize=14, fontweight='bold')
# ax2.grid(True, alpha=0.3, linestyle='--')

# ax3 = plt.subplot(1, 3, 3)
# colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(densities)))
# bars = ax3.bar([f'{d:.2f}' for d in densities], times_vs_density,
#                color=colors, edgecolor='black', linewidth=1.5, alpha=0.8)
# ax3.set_xlabel('Edge Density', fontsize=13, fontweight='bold')
# ax3.set_ylabel('Execution Time (ms)', fontsize=13, fontweight='bold')
# ax3.set_title('Time Distribution Across Densities', fontsize=14, fontweight='bold')
# ax3.grid(True, alpha=0.3, linestyle='--')
# plt.xticks(rotation=45)
# plt.suptitle(f"Dijkstra's Algorithm with Varying Edge Densities (|V|={V_fixed})",
#              fontsize=16, fontweight='bold')
# plt.tight_layout()
# plt.savefig('dijkstra_list_varying_density.png', dpi=300, bbox_inches='tight')
# plt.show()

# =========================
# EXPERIMENT 2: TIME vs NUMBER OF VERTICES FOR DIFFERENT DENSITIES
# =========================
V_values = [10, 20, 40, 60, 80, 100, 150, 200]  # can extend
densities = [0.05, 0.1, 0.3, 0.5, 0.7, 0.9]     # 6 densities → 6 lines
trials_per_run = 3

# Store execution times for each density and V
times_all = {density: [] for density in densities}
edges_all = {density: [] for density in densities}

# Run benchmarks
for density in densities:
    for V in V_values:
        avg_time, avg_edges = benchmark_dijkstra_list(V, density=density, trials=trials_per_run)
        times_all[density].append(avg_time * 1000)  # convert to ms
        edges_all[density].append(avg_edges)

# =========================
# PLOTTING: 4 SUBPLOTS
# =========================
fig, axs = plt.subplots(2, 2, figsize=(16, 10))
axs = axs.flatten()
colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(densities)))

# 1. Time vs |V|
for i, density in enumerate(densities):
    axs[0].plot(V_values, times_all[density], 'o-', color=colors[i], label=f'density={density:.2f}')
axs[0].set_xlabel('Number of Vertices |V|', fontsize=13, fontweight='bold')
axs[0].set_ylabel('Execution Time (ms)', fontsize=13, fontweight='bold')
axs[0].set_title('Time vs Number of Vertices', fontsize=14, fontweight='bold')
axs[0].grid(True, alpha=0.3, linestyle='--')
axs[0].legend()

# 2. Time normalized by log|V|
for i, density in enumerate(densities):
    normalized_time = [t/np.log2(V) for t, V in zip(times_all[density], V_values)]
    axs[1].plot(V_values, normalized_time, 's-', color=colors[i], linewidth=2, label=f'density={density:.2f}')
axs[1].set_xlabel('Number of Vertices |V|', fontsize=13, fontweight='bold')
axs[1].set_ylabel('Time / log2(|V|) (ms)', fontsize=13, fontweight='bold')
axs[1].set_title('Normalized Time vs |V|', fontsize=14, fontweight='bold')
axs[1].grid(True, alpha=0.3, linestyle='--')
axs[1].legend()

# 3. Edge growth vs |V|
for i, density in enumerate(densities):
    axs[2].plot(V_values, edges_all[density], '^-', color=colors[i], linewidth=2, label=f'density={density:.2f}')
axs[2].set_xlabel('Number of Vertices |V|', fontsize=13, fontweight='bold')
axs[2].set_ylabel('Average |E|', fontsize=13, fontweight='bold')
axs[2].set_title('Edge Growth vs |V|', fontsize=14, fontweight='bold')
axs[2].grid(True, alpha=0.3, linestyle='--')
axs[2].legend()

# 4. Time vs |V| log|V| (theoretical reference)
for i, density in enumerate(densities):
    ref_time = [e * np.log2(V) for e, V in zip(edges_all[density], V_values)]
    axs[3].plot(V_values, ref_time, '--', color=colors[i], label=f'density={density:.2f}')
axs[3].set_xlabel('Number of Vertices |V|', fontsize=13, fontweight='bold')
axs[3].set_ylabel('|E| log2(|V|)', fontsize=13, fontweight='bold')
axs[3].set_title('Reference: |E| log|V|', fontsize=14, fontweight='bold')
axs[3].grid(True, alpha=0.3, linestyle='--')
axs[3].legend()

plt.suptitle(f"Dijkstra's Algorithm Performance Across Densities (Varying |V|)", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 80)
print("FINAL SUMMARY")
print("=" * 80)
print("""
DIJKSTRA'S ALGORITHM - ADJACENCY LIST & MIN-HEAP PRIORITY QUEUE
================================================================""")
