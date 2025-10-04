import time
import math
import matplotlib.pyplot as plt
from graph_func import graph_generator, convert_to_adjacency_list
from measure_runtime import measure_runtime, measure_runtime2
from dijkstra_matrix_array import dijkstra_matrix_array
from dijkstra_list_heap import dijkstra_list_heap

# -------------------------------
# Part A: Dijkstra using Adj Matrix
# -------------------------------

def plot_partA_complete_graph():
    complete_arr = {"x": [], "y": []}

    for n in range(4, 101):
        complete_arr["x"].append(n)
        e = n * (n - 1)
        adj_mat = graph_generator(n, e)

        startTime = time.perf_counter()
        dijkstra_matrix_array(adj_mat, 0)
        stopTime = time.perf_counter()

        runtime = (stopTime - startTime) * 1000
        complete_arr["y"].append(runtime)

    scaling_fac = 0.0001
    theor_runtime = [n ** 2 * scaling_fac for n in complete_arr["x"]]

    plt.figure(figsize=(15, 10))
    plt.plot(complete_arr["x"], complete_arr["y"], label="Complete Graph", color="blue")
    plt.plot(complete_arr["x"], theor_runtime, label="Theoretical Runtime (O(V^2))", color="red", linestyle="--")
    plt.xlabel("Number of vertices (n)")
    plt.ylabel("Time Taken (ms)")
    plt.title("Runtime of Dijkstra using Adj Matrix [Complete Graph]")
    plt.grid()
    plt.legend()
    plt.show()

    return complete_arr

# ------------------------------------------
# Dijkstra runtime vs number of edges, V=10
# ------------------------------------------
def plot_edges_runtime_V10():
    V = 10 
    max_edges = V * (V - 1)  
    
    edges_range = list(range(1, max_edges + 1))  
    emp_times = []
    theor_times = []

    for E in edges_range:
        total_time = sum(measure_runtime(V, E) for _ in range(5)) / 5
        emp_times.append(total_time)
        theor_times.append((V ** 2) * (10 ** -6) * 0.3) 
    
    scaling_fac = emp_times[1] / theor_times[1] if len(theor_times) > 1 else 1
    scaled_theor_times = [t * scaling_fac for t in theor_times]

    plt.figure(figsize=(10, 6))
    plt.plot(edges_range, emp_times, 'bo-', label='Empirical Running Time (Averaged)')
    plt.plot(edges_range, scaled_theor_times, 'r--x', label='Scaled Theoretical Running Time')
    plt.title("Dijkstra (Matrix+Array) Runtime vs. Number of Edges (Averaged), V=10")
    plt.xlabel("Number of Edges")
    plt.ylabel("Running Time (seconds)")
    plt.legend()
    plt.grid()
    plt.show()

# ------------------------------------------
# Dijkstra runtime vs number of edges, V=100
# ------------------------------------------
def plot_edges_runtime_V100():
    V = 100  
    max_edges = V * (V - 1)  
        
    edges_range = list(range(1, max_edges + 1, 100))  
    emp_times = []
    theor_times = []

    for E in edges_range:
        total_time = sum(measure_runtime(V, E) for _ in range(5)) / 5  
        emp_times.append(total_time)

    theor_times = [(V ** 2) * (10 ** -6) * 0.3 for _ in edges_range] 
    scaling_fac = emp_times[10] / theor_times[10] if len(theor_times) > 1 else 1
    scaled_theor_times = [t * scaling_fac for t in theor_times]

    plt.figure(figsize=(10, 6))
    plt.plot(edges_range, emp_times, 'bo-', label='Empirical Running Time (Averaged)')
    plt.plot(edges_range, scaled_theor_times, 'r--x', label='Scaled Theoretical Running Time')
    plt.title("Dijkstra (Matrix+Array) Runtime vs. Number of Edges, V=100")
    plt.xlabel("Number of Edges")
    plt.ylabel("Running Time (seconds)")
    plt.legend()
    plt.grid()
    plt.show() 

# ------------------------------------------
# Dijkstra runtime vs number of nodes, E=10
# ------------------------------------------
def plot_nodes_runtime_E10():
    E = 10
    node_range = list(range(4, 101)) 
    emp_times = []
    theor_times = []

    for V in node_range:
        total_time = sum(measure_runtime(V, E) for _ in range(5)) / 5
        emp_times.append(total_time)
        theor_times.append((V ** 2) * (10 ** -6))

    scaling_fac = emp_times[60] / theor_times[60] if len(theor_times) > 1 else 1
    scaled_theor_times = [t * scaling_fac for t in theor_times]

    plt.figure(figsize=(10, 6))
    plt.plot(node_range, emp_times, 'bo-', label='Empirical Running Time (Averaged)')
    plt.plot(node_range, scaled_theor_times, 'r--x', label='Scaled Theoretical Running Time')
    plt.title("Dijkstra (Matrix+Array) Runtime vs. Number of Nodes (Averaged), E=10")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Running Time (seconds)")
    plt.legend()
    plt.grid()
    plt.show()

# ------------------------------------------
# Dijkstra runtime vs number of nodes, E=100
# ------------------------------------------
def plot_nodes_runtime_E100():
    E = 100
    node_range = list(range(11, 200)) 
    emp_times = []
    theor_times = []

    for V in node_range:
        total_time = sum(measure_runtime(V, E) for _ in range(5)) / 5
        emp_times.append(total_time)
        theor_times.append((V ** 2) * (10 ** -6))

    scaling_fac = emp_times[100] / theor_times[100] if len(theor_times) > 1 else 1
    scaled_theor_times = [t * scaling_fac for t in theor_times]

    plt.figure(figsize=(10, 6))
    plt.plot(node_range, emp_times, 'bo-', label='Empirical Running Time (Averaged)')
    plt.plot(node_range, scaled_theor_times, 'r--x', label='Scaled Theoretical Running Time')
    plt.title("Dijkstra (Matrix+Array) Runtime vs. Number of Nodes (Averaged), E=100")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Running Time (seconds)")
    plt.legend()
    plt.grid()
    plt.show()

# ------------------------------------------
# Dijkstra runtime vs number of edges, E=1000
# ------------------------------------------
def plot_nodes_runtime_E1000():
    E = 1000
    node_range = list(range(50, 301)) 
    emp_times = []
    theor_times = []

    for V in node_range:
        total_time = sum(measure_runtime(V, E) for _ in range(5)) / 5
        emp_times.append(total_time)
        theor_times.append((V ** 2) * (10 ** -6))

    scaling_fac = emp_times[100] / theor_times[100] if len(theor_times) > 1 else 1
    scaled_theor_times = [t * scaling_fac for t in theor_times]

    plt.figure(figsize=(10, 6))
    plt.plot(node_range, emp_times, 'bo-', label='Empirical Running Time (Averaged)')
    plt.plot(node_range, scaled_theor_times, 'r--x', label='Scaled Theoretical Running Time')
    plt.title("Dijkstra (Matrix+Array) Runtime vs. Number of Nodes (Averaged), E=1000")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Running Time (seconds)")
    plt.legend()
    plt.grid()
    plt.show()

# ------------------------------------------
# Part B: Dijkstra using adjacency list + heap
# ------------------------------------------
def plot_partB_complete_graph():
    complete_list = {"x": [], "y": []}

    for n in range(50, 201):
        complete_list["x"].append(n)
        e = n * (n - 1)
        adj_mat = graph_generator(n, e)
        adj_list = convert_to_adjacency_list(adj_mat, n)

        startTime = time.perf_counter()
        dijkstra_list_heap(adj_list, 0)
        stopTime = time.perf_counter()

        runtime = (stopTime - startTime) * 1000
        complete_list["y"].append(runtime)

    plt.figure(figsize=(15, 10))
    plt.plot(complete_list["x"], complete_list["y"], label="Complete Graph", color="blue")
    plt.xlabel("Number of vertices (n)")
    plt.ylabel("Time Taken (ms)")
    plt.title("Runtime of Dijkstra using Adj List and heap [Complete Graph]")
    plt.grid()
    plt.legend()
    plt.show()

    return complete_list

# ------------------------------------------
# Dijkstra runtime vs number of edges, V=10
# ------------------------------------------
def plot_partB_edges_runtime_V10():
    V = 10
    max_edges = V * (V - 1)

    edges_range = list(range(1, max_edges + 1))
    emp_times = []
    theor_times = []

    for E in edges_range:
        total_time = sum(measure_runtime2(V, E) for _ in range(5)) / 5
        emp_times.append(total_time)
        theor_times.append((E + V) * math.log(V+1) * (10 ** -6)) 

    scaling_fac = emp_times[1] / theor_times[1] if len(theor_times) > 1 else 1
    scaled_theor_times = [t * scaling_fac for t in theor_times]

    plt.figure(figsize=(10, 6))
    plt.plot(edges_range, emp_times, 'bo-', label='Empirical Running Time (Averaged)')
    plt.plot(edges_range, scaled_theor_times, 'r--x', label='Scaled Theoretical Runtime (O((V+E)logV))')
    plt.title("Dijkstra (List+Heap) Runtime vs. Number of Edges, V=10")
    plt.xlabel("Number of Edges")
    plt.ylabel("Running Time (seconds)")
    plt.legend()
    plt.grid()
    plt.show()

# ------------------------------------------
# Dijkstra runtime vs number of edges, V=100
# ------------------------------------------
def plot_partB_edges_runtime_V100():
    V = 100
    max_edges = V * (V - 1)

    edges_range = list(range(1, max_edges + 1, 100))  
    emp_times = []
    theor_times = []

    for E in edges_range:
        total_time = sum(measure_runtime2(V, E) for _ in range(5)) / 5
        emp_times.append(total_time)
        theor_times.append((E + V) * math.log(V + 1) * (10 ** -6)) 

    scaling_fac = emp_times[10] / theor_times[10] if len(theor_times) > 10 else 1
    scaled_theor_times = [t * scaling_fac for t in theor_times]

    plt.figure(figsize=(10, 6))
    plt.plot(edges_range, emp_times, 'bo-', label='Empirical Running Time (Averaged)')
    plt.plot(edges_range, scaled_theor_times, 'r--x', label='Scaled Theoretical Runtime (O((V+E)logV))')
    plt.title("Dijkstra (List+Heap) Runtime vs. Number of Edges, V=100")
    plt.xlabel("Number of Edges")
    plt.ylabel("Running Time (seconds)")
    plt.legend()
    plt.grid()
    plt.show()

# ------------------------------------------
# Dijkstra runtime vs number of nodes, E=10
# ------------------------------------------
def plot_partB_nodes_runtime_E10():
    E = 10
    node_range = list(range(4, 101))
    emp_times = []
    theor_times = []

    for V in node_range:
        total_time = sum(measure_runtime2(V, E) for _ in range(5)) / 5
        emp_times.append(total_time)
        theor_times.append((E + V) * math.log(V+1) * (10 ** -6))

    scaling_fac = emp_times[10] / theor_times[10] if len(theor_times) > 10 else 1
    scaled_theor_times = [t * scaling_fac for t in theor_times]

    plt.figure(figsize=(10, 6))
    plt.plot(node_range, emp_times, 'bo-', label='Empirical Running Time (Averaged)')
    plt.plot(node_range, scaled_theor_times, 'r--x', label='Scaled Theoretical Running Time (O((V+E)logV))')
    plt.title("Dijkstra (List+Heap) Runtime vs. Number of Nodes, E=10")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Running Time (seconds)")
    plt.legend()
    plt.grid()
    plt.show()

# ------------------------------------------
# Dijkstra runtime vs number of nodes, E=100
# ------------------------------------------
def plot_partB_nodes_runtime_E100():
    E = 100
    node_range = list(range(11, 200))
    emp_times = []
    theor_times = []

    for V in node_range:
        total_time = sum(measure_runtime2(V, E) for _ in range(5)) / 5
        emp_times.append(total_time)
        theor_times.append((E + V) * math.log(V+1) * (10 ** -6))

    scaling_fac = emp_times[50] / theor_times[50] if len(theor_times) > 50 else 1
    scaled_theor_times = [t * scaling_fac for t in theor_times]

    plt.figure(figsize=(10, 6))
    plt.plot(node_range, emp_times, 'bo-', label='Empirical Running Time (Averaged)')
    plt.plot(node_range, scaled_theor_times, 'r--x', label='Scaled Theoretical Running Time (O((V+E)logV))')
    plt.title("Dijkstra (List+Heap) Runtime vs. Number of Nodes, E=100")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Running Time (seconds)")
    plt.legend()
    plt.grid()
    plt.show()


# ------------------------------------------
# Dijkstra runtime vs number of nodes, E=1000
# ------------------------------------------
def plot_partB_nodes_runtime_E1000():
    E = 1000
    node_range = list(range(50, 301))
    emp_times = []
    theor_times = []

    for V in node_range:
        total_time = sum(measure_runtime2(V, E) for _ in range(5)) / 5
        emp_times.append(total_time)
        theor_times.append((E + V) * math.log(V+1) * (10 ** -6))

    scaling_fac = emp_times[100] / theor_times[100] if len(theor_times) > 100 else 1
    scaled_theor_times = [t * scaling_fac for t in theor_times]

    plt.figure(figsize=(10, 6))
    plt.plot(node_range, emp_times, 'bo-', label='Empirical Running Time (Averaged)')
    plt.plot(node_range, scaled_theor_times, 'r--x', label='Scaled Theoretical Running Time (O((V+E)logV))')
    plt.title("Dijkstra (List+Heap) Runtime vs. Number of Nodes, E=1000")
    plt.xlabel("Number of Nodes")
    plt.ylabel("Running Time (seconds)")
    plt.legend()
    plt.grid()
    plt.show()


# ------------------------------------------
# Combined CPU time: Array vs List
# ------------------------------------------
def plot_cpu_time_comparison(complete_arr, complete_list):
    plt.figure(figsize=(15, 10))
    plt.plot(complete_arr["x"], complete_arr["y"], label="Array", color="red")
    plt.plot(complete_list["x"], complete_list["y"], label="List", color="green")
    plt.xlabel("Number of vertices (n)")
    plt.ylabel("Time (ms)")
    plt.title("Comparison of CPU Time: Adj Matrix vs. Adj List [Complete Graph]")
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    #part A
    complete_arr = plot_partA_complete_graph()

    #part a fixed V
    plot_edges_runtime_V10()
    plot_edges_runtime_V100()

    #part a fixed E
    plot_nodes_runtime_E10()
    plot_nodes_runtime_E100()
    plot_nodes_runtime_E1000()

    #part B
    complete_list = plot_partB_complete_graph()

    #part b fixed V
    plot_partB_edges_runtime_V10()
    plot_partB_edges_runtime_V100()

    #part b fixed E
    plot_partB_nodes_runtime_E10()
    plot_partB_nodes_runtime_E100()
    plot_partB_nodes_runtime_E1000()

    #part c 
    plot_cpu_time_comparison(complete_arr, complete_list)

    print("All 13 plots generated")