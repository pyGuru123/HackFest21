from sys import stdin

def spiralPrint(mat,nRows,mCols):
    if nRows==0:
        return
    
    rowStart,colStart=0,0
    numElements=nRows*mCols
    count=0
    
    while count<numElements:
        i=colStart
        while i<mCols and count < numElements:
            print(mat[rowStart][i],end=" ")
            count+=1
            i+=1
        rowStart+=1
        i= rowStart
        while i<nRows and count<numElements:
            print(mat[i][mCols-1],end=" ")
            count+=1
            i+=1
        mCols-=1
        i= mCols-1
        while i>=colStart and count<numElements:
            print(mat[nRows-1][i],end=" ")
            count+=1
            i-=1
        nRows-=1
        i=nRows-1
        while i>=rowStart and count<numElements:
            print(mat[i][colStart],end=" ")
            count+=1
            i-=1
        colStart+=1
        
        
    
#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(input())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()
    t -= 1
