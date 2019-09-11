from collections import deque
n=4
vertices=[[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]]
sv=0
visited=[False]*n
def BFS(sv):
    # if visited[sv]==False:
    #     visited[sv]=True
    #     print(sv,end=" ")
    q=[]
    # for i in vertices[sv]:
    #     if i==1:
    #         q.append(sv+1)
    q.append(sv)
    while(q!=[]):
        x=q.pop(0)
        if visited[x]==False:
            visited[x]=True
            print(x)
        for i in range(len(vertices[x])):
            if vertices[x][i] == 1:
                if visited[i]==False:
                    q.append(i)
BFS(sv)