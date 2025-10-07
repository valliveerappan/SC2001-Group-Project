import heapq
from collections import defaultdict
from numpy import inf

def dijkstra_list_heap(graph: dict, start: int):
    n = max(max(graph.keys()), max((v for neighbors in graph.values() for v, _ in neighbors))) + 1

    distances = [inf] * n
    distances[start] = 0
    visited = [False] * n
    parent = [-1] * n

    #min heap priority queue (distance, vertex)
    heap = [(0, start)]

    while heap:
        current_distance, u = heapq.heappop(heap)

        if visited[u]:
            continue
        visited[u] = True

        for neighbor, weight in graph[u]:
            if not visited[neighbor]:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    parent[neighbor] = u
                    heapq.heappush(heap, (new_distance, neighbor))

    return distances, parent

