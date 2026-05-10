import heapq

def prim_mst(graph, start=0):
    mst = []
    visited = [False] * len(graph)
    min_heap = [(0, start)]
    total_weight = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)

        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
                mst.append((u, v, w))

    return mst, total_weight

# 🔸 Dynamic input
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = {i: [] for i in range(n)}
print("Enter each edge in the format: u v w (0-based indexing)")
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # Undirected graph

mst, weight = prim_mst(graph)
print("\nPrim's MST edges:")
for u, v, w in mst:
    print(f"{u} -- {v} == {w}")
print("Total weight of MST:", weight)
