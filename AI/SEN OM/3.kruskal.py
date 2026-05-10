def find(parent,i):
    while parent[i]!=i:
        i=parent[i]
    return i
    
def union(parent,u,v):
    parent[find(parent,u)]=find(parent,v)
    
V=int(input('enter the no  Vertices '))
E=int(input('enter the no  Edges'))

edges=[]

for i in range(E):
    u,v,w=input(f'enter the edge {i+1} (u,v,w)').split()
    edges.append((int(w),int(u),int(v)))
    
parent=list(range(V))
edges.sort()

print('\n edges : weight')
total_weight=0

for w,u,v in edges:
    if find(parent,u)!=find(parent,v):
        union(parent,u,v)
        print(u,'-',v,':',w)
        total_weight+=w
        
        if len(set(find(parent,i) for i in range(V)))==1:
            break
        
print('\n total weight : ',total_weight)
    
