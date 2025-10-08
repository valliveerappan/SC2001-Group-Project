from graph_utils import INF
import heapq

def dijkstra_list_heap(adj_list, start):
    d = {node: INF for node in adj_list.keys()}
    d[start] = 0
    pi = {node: None for node in adj_list.keys()}
    S = set()

    heap = []
    heapq.heappush(heap, (0, start))

    while heap and len(S) < len(adj_list):
        dist_u, u = heapq.heappop(heap)
        if u in S:
            continue
        S.add(u)

        for v, w in adj_list[u]:
            if v in S:
                continue
            new_dist = dist_u + w
            if new_dist < d[v]:
                d[v] = new_dist
                pi[v] = u
                heapq.heappush(heap, (d[v], v))

    return d, pi, S
