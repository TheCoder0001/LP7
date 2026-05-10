import heapq

# User input for graph
graph = {}
n = int(input("Enter number of edges: "))
print("Enter each edge as: Node1 Node2 Cost")

for _ in range(n):
    u, v, cost = input().split()
    cost = int(cost)

    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append((v, cost))
    graph[v].append((u, cost))  # undirected graph

# User input for heuristics
heuristic = {}
nodes = set(graph.keys())
print("\nEnter heuristic values for each node:")

for node in nodes:
    h = int(input(f"Heuristic for {node}: "))
    heuristic[node] = h

# A* Algorithm
def astar(graph, start, goal, heuristic):
    open_set = [(heuristic[start], 0, start, [start])]  # (f, g, node, path)
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            return path, g

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))

    return None, None

# Start and goal input
start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

# Run A*
path, total_cost = astar(graph, start, goal, heuristic)

# Output
print()
if path:
    print("Shortest path from", start, "to", goal, ":", " -> ".join(path))
    print("Total cost:", total_cost)
else:
    print("No path found.")
