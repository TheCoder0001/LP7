import heapq

# Graph with weighted edges
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 1), ('D', 3)],
    'C': [('A', 4), ('B', 1)],
    'D': [('B', 3)]
}
# Heuristic estimates to goal node 'D'
heuristic = {
    'A': 4,
    'B': 2,
    'C': 3,
    'D': 0
}
# A* Algorithm
def astar(graph, start, goal, heuristic):
    open_set = [(heuristic[start], 0, start, [start])]  # (f, g, node, path)
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            return path, g  # Return path and total cost

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return None, None
# Main
start = 'A'
goal = 'D'

path, total_cost = astar(graph, start, goal, heuristic)

# Direct Output
if path:
    print("Shortest path from", start, "to", goal, ":", " -> ".join(path))
    print("Total cost:", total_cost)
else:
    print("No path found.")
