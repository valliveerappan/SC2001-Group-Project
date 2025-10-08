import random

INF = float('inf')

def gen_matrix(n, p=0.3, seed=42):
    random.seed(seed)
    W = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        W[i][i] = 0
        added_edge = False
        for j in range(n):
            if i != j and random.random() < p:
                W[i][j] = random.randint(1, 10)
                added_edge = True
        if not added_edge:
            j = random.choice([k for k in range(n) if k != i])
            W[i][j] = random.randint(1, 10)
    return W

def count_edges_matrix(W):
    n = len(W)
    edge_count = 0
    for i in range(n):
        for j in range(n):
            if i != j and W[i][j] != INF:
                edge_count += 1
    return edge_count

def gen_graph_connected(V, seed=42, avg_deg=3, weight_range=(1,10)):
    random.seed(seed)
    E_target = V * avg_deg
    E_max = V * (V - 1)
    E_target = min(E_target, E_max)

    g = {u: [] for u in range(1, V+1)}
    edges = set()

    order = list(range(1, V+1))
    random.shuffle(order)
    for i in range(V - 1):
        u, v = order[i], order[i+1]
        if (u, v) not in edges:
            w = random.randint(*weight_range)
            g[u].append((v, w))
            edges.add((u, v))

    candidates = [(u, v) for u in range(1, V+1) for v in range(1, V+1) if u != v and (u, v) not in edges]
    random.shuffle(candidates)

    need = E_target - len(edges)
    for i in range(max(0, need)):
        u, v = candidates[i]
        w = random.randint(*weight_range)
        g[u].append((v, w))
        edges.add((u, v))

    E_actual = len(edges)
    return g, E_actual
