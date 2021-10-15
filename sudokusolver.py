def next_empty_space(puzzle):
    #finds the next row, col that is empty ;; returns (row,col) or ((None,None) if empty)

    for r in range(9):
        for c in range(9):
            if puzzle[r][c]==-1:
                return r,c
    
    return None, None    #if no space is empty


def is_valid(puzzle,guess,row,col):

    #checks the guess at row of the puzzle is valid
    row_vals= puzzle[row]
    if guess in row_vals:
        return False

    #checks the guess at col of puzzle is valid
    col_vals=[puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    #checks in 3X3 matrix
    row_start= (row//3)*3
    col_start= (col//3)*3

    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if puzzle[r][c]==guess:
                return False
    
    return True
    

def solve_sudoku(puzzle):
    #solve sudoku using backtracking
    #puzzle is a list of lists where each row is the inner list
    row, col= next_empty_space(puzzle)

    #when theres no free space left that means our puzzle is complete
    if row is None:
        return True
    
    #if theres a free space then guess between 1 to 9
    for guess in range(1,10): 
        if is_valid(puzzle,guess,row,col):         #check if the guess is valid
            puzzle[row][col]=guess
        
            #recursively calls the function
            if solve_sudoku(puzzle):
                return True

        #if not valid then we need to backtrack and try a new number
        puzzle[row][col]= -1

    #if this puzzle is unsolvable
    return False

if __name__ == '__main__':
    example_board= [
        [-1,-1,-1, -1,-1,-1, 2,-1,-1],
        [-1,8,-1, -1,-1,7, -1,9,-1],
        [6,-1,2, -1,-1,-1, 5,-1,-1],
        
        [-1,7,-1, -1,6,-1, -1,-1,-1],
        [-1,-1,-1, 9,-1,1, -1,-1,-1],
        [-1,-1,-1, -1,2,-1, -1,4,-1],

        [-1,-1,5, -1,-1,-1, 6,-1,3],
        [-1,9,-1, 4,-1,-1, -1,7,-1],
        [-1,-1,6, -1,-1,-1, -1,-1,-1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)