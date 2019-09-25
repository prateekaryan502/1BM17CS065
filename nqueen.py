def nqueen(x,col,n):
    if col>=n:
        return True
    for i in range(n):
        if queenunderattack(x,i,col,n):
            x[i][col]=1
            if nqueen(x,col+1,n)==True:
                print(x)
            x[i][col]=0
    return False
def queenunderattack(x,row,col,n):
    for i in range(col):
        if x[row][i]==1:
            return  False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if x[i][j]==1:

            return  False
    for i,j in zip(range(row,n,1),range(col,-1,-1)):
        if x[i][j]==1:

            return False
    return True
n=int(input("Enter number of queens"))
x=[[0 for i in range(n)] for j in range(n) ]
nqueen(x,0,n)
