vertices=[[0,0,1,0,0],[0,0,1,0,0],[1,1,0,0,0],[0,0,0,0,1],[0,0,0,1,0]]
visited=[]
def DFS(i,v):
    visited[i]=True
    print(i+1,end=" ")
    for i in range(len(v)):
        if v[i]==1 and visited[i]==False:
            DFS(i,vertices[i])

for i in vertices:
    visited.append(False)

for i in range(len(vertices)):
    if visited[i]==False:
        DFS(i,vertices[i])
        print(" ")

