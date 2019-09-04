matrix=[[1,0,1,0,1],[1,1,0,0,0],[0,1,0,1,1],[0,0,0,0,0],[0,0,0,0,0]]#,[0,1,1,1,1],[1,0,1,0,0]]

count =0
visited=[]
for i in range(len(matrix)):
    visited.append([])
    for j in range(len((matrix[i]))) :
        visited[i].append(False)


def DFS(matrix,i,j,visited):

    visited[i][j]=True
    for m in range(i-1,i+2):
        for n in range(j-1,j+2):
            if m>= 0 and n>= 0 and m < len(matrix) and n < len(matrix) and visited[m][n]==False and matrix[m][n]==1:

                DFS(matrix,m,n,visited)


for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j]==1 and visited[i][j]==False :
            DFS(matrix,i,j,visited)
            count+=1

print(count)
