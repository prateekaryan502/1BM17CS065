matrix=[[1,0,1,0,1],[1,1,1,1,0],[0,1,1,1,1],[0,1,1,1,1],[1,0,1,0,0]]
for i in matrix:
    print(i)
count =0
visited=[]
for i in range(len(matrix)):
    visited.append([])
    for j in range(len((matrix[i]))) :
        visited[i].append(False)

print(visited)
def DFS(matrix,i,j,visited):
    print(i,j,count)
    visited[i][j]=True
    for m in range(i-1,i+2):
        for n in range(j-1,j+2):
            if m-1 >= 0 and n - 1 >= 0 and m+1 < len(matrix) and n + 1 <= len(matrix) and visited[m][n]==False:
                print(m,n,"in")
                DFS(matrix,m,n,visited)
            else:
                print(m,n,"not in")
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j]==1 and visited[i][j]==False :
            DFS(matrix,i,j,visited)
            count+=1

print(count)
print(visited)
