def check_connectivity(graph):
    if not graph:
        return True

    start_node = next(iter(graph))
    visited = set()
    stack = [start_node]
    
    while stack:
        current_node = stack.pop()
        
        if current_node not in visited:
            visited.add(current_node)
            
            if current_node in graph:
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
                        
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors)

    return len(visited) == len(all_nodes)

# --- Демонстраційний код ---
graph_B = {
    1: [2, 4],
    2: [1, 3],
    3: [2, 4],
    4: [1, 3]
}

disconnected_graph = {
    1: [2],
    2: [1],
    3: [4],
    4: [3]
}

print(check_connectivity(graph_B))
print(check_connectivity(disconnected_graph))
