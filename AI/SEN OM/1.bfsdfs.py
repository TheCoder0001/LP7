#dfs
def dfs(visited,graph,node):
	if node not in visited:
		print(node,end=" ")
		visited.add(node)
#recursive call
		for neighbour in graph[node]:
			dfs(visited,graph,neighbour)
			
#bfs
def bfs(visited,graph,node,queue):
	visited.add(node) 	#start node add to visited 
	queue.append(node)	#start node added to queue
	
	while queue:		# for all nodes
		s=queue.pop(0)	# pop the node FIFO
		print(s,end=" ")	# print the popped node
		
		for neighbour in graph[s]:	#same for other nodes
			if neighbour not in visited:
				visited.add(neighbour)
				queue.append(neighbour)
				
#input
		
graph ={}
n=int(input("enter the number of nodes "))
for i in range(n):
	entry=input("enter the node followed by their child ").split()
	node, *children=entry
	graph[node]=children

start=input("enter the start node : ").strip()

print("\nDFS ")
dfs(set(),graph,start)

print("\nBFS ")
bfs(set(),graph,start,[])
