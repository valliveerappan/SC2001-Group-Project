from graph_utils import INF

def dijkstra_matrix(W, start_idx):
    n = len(W)
    d = [INF] * n
    pi = [None] * n
    visited = [False] * n

    d[start_idx] = 0

    for _ in range(n):
        u = None
        min_dist = INF
        for x in range(n):
            if not visited[x] and d[x] < min_dist:
                min_dist = d[x]
                u = x

        if u is None:
            break

        visited[u] = True

        for v in range(n):
            w = W[u][v]
            if w != INF and not visited[v]:
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
                    pi[v] = u

    d_1 = {i + 1: d[i] for i in range(n)}
    pi_1 = {i + 1: (pi[i] + 1 if pi[i] is not None else None) for i in range(n)}
    S_1 = {i + 1 for i in range(n) if visited[i]}
    return d_1, pi_1, S_1
