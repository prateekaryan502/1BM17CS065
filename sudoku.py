import math
sudoku = [[0, 0, 3, 4], [3, 4, 0, 0], [0, 0, 4, 3], [0, 3, 2, 0]]
def rowissafe(sudoku,row,value):
    for i in range(4):
        if sudoku[row][i]==value:
            return False
    return True
def columnissafe(sudoku,col,value):
    for i in range(4):
        if sudoku[i][col]==value:
            return False
    return  True
def gridissafe(sudoku,row,col,value):
    x=int(row-(row%(math.sqrt(len(sudoku)))))
    y=int(col-(col%(math.sqrt(len(sudoku)))))
    for i in range(4):
        for j in range(4):
            if sudoku[i+x][j+y]==value:
                print("dfji")
                return False
    return True
def checklocationissafe(sudoku,row,col,num):
    if rowissafe(sudoku,row,num) and columnissafe(sudoku,col,num) and gridissafe(sudoku,row,col,num):
        print(num,"jfkd")
        return True
    else :
        return False
def unassigned(sudoku,l):
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j]==0 :
                l[0]=i
                l[1]=j
            return True

    return False

def solvesudoku(sudoku):

    l=[0,0]
    if (not unassigned(sudoku,l)):
        return True
    row=l[0]
    col=l[1]
    print(row,col)
    for i in range(1,len(sudoku)+1):
        if (checklocationissafe(sudoku,row,col,i)):
            sudoku[row][col]=i
            if(solvesudoku(sudoku)):
                return True
            sudoku[row][col]=0
    return False

#print(solvesudoku(sudoku))
solvesudoku(sudoku)
print(sudoku)
