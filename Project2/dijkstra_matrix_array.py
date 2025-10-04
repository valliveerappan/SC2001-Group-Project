def dijkstra_matrix_array(graph, start):
    n = len(graph)
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
        
        # STEP 2: Update distances for neighbors
        # Due to adjacency matrix, we check ALL vertices
        for v in range(n):
            weight = graph[current_vertex][v]
            if weight > 0 and not visited[v]:
                new_distance = distances[current_vertex] + weight
                if new_distance < distances[v]:
                    distances[v] = new_distance
                    parent[v] = current_vertex
    
    return distances, parent


# def reconstruct_path(parent, start, end):
#     """Reconstruct shortest path from start to end."""
#     if parent[end] == -1 and start != end:
#         return None
    
#     path = []
#     current = end
#     while current != -1:
#         path.append(current)
#         current = parent[current]
    
#     return list(reversed(path))