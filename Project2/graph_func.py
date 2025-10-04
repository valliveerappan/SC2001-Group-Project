import random
from collections import defaultdict

def graph_generator(n, e):
    matrix = [[0 for i in range(n)] for j in range(n)]
    while e != 0:
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        if a != b and matrix[a][b] == 0:
            matrix[a][b] = 1
            e -= 1

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                matrix[i][j] = random.randint(1, 100)
    return matrix

def convert_to_adjacency_list(graph, n):
    adjacency_list = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                adjacency_list[i].append((j, graph[i][j]))
    return adjacency_list
