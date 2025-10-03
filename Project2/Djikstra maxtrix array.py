def dijkstra_matrix_array(graph, start):
    n = graph.num_vertices
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
        
        # STEP 2: Update distances to neighbors - O(|V|)
        # Due to adjacency matrix, we check ALL vertices
        for neighbor in range(n):
            if graph.graph[current_vertex][neighbor] > 0 and not visited[neighbor]:
                new_distance = distances[current_vertex] + graph.graph[current_vertex][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    parent[neighbor] = current_vertex
    
    return distances, parent