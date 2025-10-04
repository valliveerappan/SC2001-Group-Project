import time
from graph_func import graph_generator, convert_to_adjacency_list
from dijkstra_matrix_array import dijkstra_matrix_array
from dijkstra_list_heap import dijkstra_list_heap

def measure_runtime(n, e):
    graph = graph_generator(n, e)
    start_time = time.time()
    dijkstra_matrix_array(graph, 0)
    end_time = time.time()
    return end_time - start_time

def measure_runtime2(V, E):
    E = min(E, V * (V - 1))
    adj_mat = graph_generator(V, E)
    adj_list = convert_to_adjacency_list(adj_mat, V)

    for i in range(V):
        adj_list[i] = [n for n in adj_list[i] if 0 <= n[0] < V]

    start = time.perf_counter()
    dijkstra_list_heap(adj_list, 0)
    end = time.perf_counter()

    return end - start


# def measure_runtime2(n, e):
#     graph = graph_generator(n, e)
#     adj_list = convert_to_adjacency_list(graph, n)
#     start_time = time.time()
#     dijkstra_list_heap(adj_list, 0)
#     end_time = time.time()
#     return end_time - start_time