import time
from graph_func import graph_generator
from dijkstra_matrix_array import dijkstra_matrix_array
from dijkstra_list_heap import dijkstra_list_heap

def measure_runtime(n, e):
    graph = graph_generator(n, e)
    start_time = time.time()
    dijkstra_matrix_array(graph, 0)
    end_time = time.time()
    return end_time - start_time

def measure_runtime2(n, e):
    graph = graph_generator(n, e)
    start_time = time.time()
    dijkstra_list_heap(graph, 0)
    end_time = time.time()
    return end_time - start_time
