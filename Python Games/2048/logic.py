# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# libraries and modules required

import random


# %%
# function for : when game is started

def startGame():
    matrix= [[0 for i in range(4)] for i in range(4)]
    return matrix


# %%
# function for : adding new "2" in the matrix at empty position

def addNew2(matrix):
    row,colunm=random.randint(0,3),random.randint(0,3)
    while matrix[row][colunm] != 0:
        row,colunm=random.randint(0,3),random.randint(0,3)

    matrix[row][colunm]=2


# %%
# function for : current status of matrix

def currStatus(matrix):
    # if any cell is having "2048",that mean game is over and "player won"
    for i in range(4):
        for j in range(4):
            if matrix[i][j]==2048:
                return "Player won"
# ---------------------------------------------------------------------------------------------------------------------------------------------
    # if any cell in the matrix is empty(ie, 0) , that mean "Game is not over yet"
    for i in range(4):
        for j in range(4):
            if matrix[i][j]==0:
                return "Game is not over"
# ---------------------------------------------------------------------------------------------------------------------------------------------
    # if all cells in matrix is filled
    for i in range(3):
        for j in range(3):
            if (matrix[i][j]==matrix[i][j+1]) or (matrix[i][j]==matrix[i+1][j]):
                return "Game is not over"

    for i in range(3):
        if matrix[3][i]==matrix[3][i+1]:
            return "Game is not over"

    for i in range(3):
        if matrix[i][3]==matrix[i+1][3]:
            return "Game is not over"
# ---------------------------------------------------------------------------------------------------------------------------------------------
    # If none of above case occure
    return "Player lost"


# %%
# function for : compression of matrix

def compress(matrix):
    changed=False
    newCompressedMatrix= [[0 for i in range(4)] for j in range(4)]

    for i in range(4):
        curr=0
        for j in range(4):
            if matrix[i][j]!=0:
                newCompressedMatrix[i][curr]=matrix[i][j]
                if curr!=j:
                    changed=True
                curr+=1

    return newCompressedMatrix,changed


# %%
# function for : merging cells which are equal and adjecent (and are not equal to "0")

def merge(matrix):
    changed=False
    for i in range(4):
        for j in range(3):
            if matrix[i][j]!=0 and (matrix[i][j]==matrix[i][j+1]):
                matrix[i][j]=(2*matrix[i][j])
                changed=True
                matrix[i][j+1]=0
    return matrix,changed


# %%
# function for : reversing rows of matrix

def reverse(matrix):
    newReversedMatrix=[]
    for i in range(4):
        newReversedMatrix.append(matrix[i][::-1])

    return newReversedMatrix


# %%
# function for : transposing matrix

def transpose(matrix):
    newTransposedMatrix=[[0 for i in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            newTransposedMatrix[j][i]=matrix[i][j]

    return newTransposedMatrix

# %% [markdown]
# ALL POSSIBLE STEPS AND THEIR STEPS TO PERFORM
# 
# # LEFT
# ### compress -> merge -> compress -> addNew2
# # RIGHT
# ### reverse -> compress -> merge -> compress -> reverse -> addNew2
# # UP
# ### transpose -> compress -> merge -> compress -> transpose -> addNew2
# # DOWN
# ### transpose -> reverse -> compress -> merge -> compress -> reverse -> transpose -> addNew2

# %%
# code for LEFT move
def leftMove(matrix):
    newMatrix,change1= compress(matrix)
    newMatrix2,change2=merge(newMatrix)
    newMatrix3,change3= compress(newMatrix2)
    # addNew2(newMatrix2)
    finalChange= (change1 or change2 or change3)
    return newMatrix3,finalChange


# %%
#  code for RIGHT move
def rightMove(matrix):
    newMatrix= reverse(matrix)
    newMatrix2,change1= compress(newMatrix)
    newMatrix3,change2=merge(newMatrix2)
    newMatrix4,change3= compress(newMatrix3)
    newMatrix5= reverse(newMatrix4)
    finalChange= (change1 or change2 or change3)
    # addNew2(newMatrix4)
    return newMatrix5,finalChange


# %%
def upMove(matrix):
    newMatrix= transpose(matrix)
    newMatrix2,change1= compress(newMatrix)
    newMatrix3,change2=merge(newMatrix2)
    newMatrix4,change3= compress(newMatrix3)
    newMatrix5= transpose(newMatrix4)
    finalChange= (change1 or change2 or change3)
    return newMatrix5,finalChange


# %%
def downMove(matrix):
    newMatrix= transpose(matrix)
    newMatrix2= reverse(newMatrix)
    newMatrix3,change1= compress(newMatrix2)
    newMatrix4,change2= merge(newMatrix3)
    newMatrix5,change3= compress(newMatrix4)
    newMatrix6= reverse(newMatrix5)
    newMatrix7= transpose(newMatrix6)
    finalChange= (change1 or change2 or change3)
    return newMatrix7,finalChange


