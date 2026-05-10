def sel():
    arr=list(map(int,input("Enter numbers").split()))
    print("OG: ",arr)
    n =len(arr)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    print("Sorted: ",arr)
# sel()
def find(p,i):
    while p[i]!=i:
        i=p[i]
    return i

def uni(p,x,y):
    p[find(p,y)]=find(p,x)

def krusk():
    n=int(input())
    e=int(input())
    edges=[]
    for i in range(e):
        u,v,wt=map(int,input().split())
        edges.append((wt,u,v))
    edges.sort()
    pa=[i for i in range(n)]
    mst=[]
    for wt,u,v in edges:
        if find(pa,u)!=find(pa,v):
            mst.append((u,v,wt))
            uni(pa,u,v)
    tc=0
    for u , v , w in mst:
        tc+=w
        print(f"{u}-->{v}={w}")
    print(tc)    
# krusk()

def main():
    flg=0
    while flg==0:
        print("1.Sel_sort\n2.Kruskals\n3.Exit")
        ch=int(input("Enter Your Choice: "))

        if ch==1:
            sel()
        elif ch==2:
            krusk()
        elif ch==3:
            flg=1
        else:
            print("enter valid choice")

main()
