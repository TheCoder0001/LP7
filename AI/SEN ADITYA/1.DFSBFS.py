from collections import deque

# Input graph from user
graph = {}
n = int(input("Enter number of edges: "))
print("Enter each edge as two space-separated nodes (e.g., A B):")
for _ in range(n):
    u, v = input().split()
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)  # Since it's an undirected graph

# Depth First Search (Recursive)
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Breadth First Search (Using Queue)
def bfs(graph, start, visited):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])

# Main
start_node = input("Enter the starting node: ")

print("DFS Traversal:")
dfs(graph, start_node, set())

print("\nBFS Traversal:")
bfs(graph, start_node, set())
