import heapq

def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    predecessors = {node: None for node in graph}
    priority_queue = [(0, start_node)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
            
        if current_node in graph:
            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
                    
    return distances, predecessors

def reconstruct_path(predecessors, start_node, end_node):
    path = []
    current = end_node
    
    while current is not None:
        path.append(current)
        current = predecessors[current]
        
        if current == start_node and start_node not in path:
            path.append(start_node)
            break
        elif current is None and path[-1] != start_node:
            return f"Шлях від {start_node} до {end_node} не знайдено."
        
    return path[::-1]

# --- Граф та його Представлення ---
# Граф:
#   (1)---4---(2)
#    |       / |
#    1     2   5
#    |   /     |
#   (4)---1---(3)---3---(5)
weighted_graph = {
    '1': {'2': 4, '4': 1},
    '2': {'1': 4, '3': 2, '5': 5},
    '3': {'2': 2, '4': 1, '5': 3},
    '4': {'1': 1, '3': 1},
    '5': {'2': 5, '3': 3}
}

start_node = '1'
end_node = '5'

# --- Виконання ---
distances, predecessors = dijkstra(weighted_graph, start_node)
shortest_path = reconstruct_path(predecessors, start_node, end_node)
shortest_distance = distances[end_node]

print(f"Найкоротша відстань від {start_node} до {end_node}: {shortest_distance}")
print(f"Шлях: {' -> '.join(shortest_path)}")
