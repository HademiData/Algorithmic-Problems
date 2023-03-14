'''

The N-Queens problem is a classic problem in computer science that involves placing N queens on an N x N 
chessboard so that no two queens attack each other. Backtracking is one of the common algorithms used to 
solve this problem. Here is an implementation of a backtracking algorithm to solve the N-Queens problem in Python:

'''

# Define a function to check if a queen can be placed in a given cell
def can_place(board, row, col, n):
    # Check row and column for other queens
    for i in range(n):
        if board[row][i] == 1 or board[i][col] == 1:
            return False
    # Check diagonals for other queens
    for i in range(n):
        for j in range(n):
            if (i+j == row+col or i-j == row-col) and board[i][j] == 1:
                return False
    # Return True if no queens attack
    return True

# Define a function to solve the N-Queens problem using backtracking
def solve_nqueens(board, col, n):
    if col >= n:
        # All queens placed, return True
        return True
    for row in range(n):
        if can_place(board, row, col, n):
            # Place queen and recursively solve remaining problem
            board[row][col] = 1
            if solve_nqueens(board, col+1, n):
                return True
            # Backtrack if queen cannot be placed
            board[row][col] = 0
    # Return False if no solution exists
    return False

# Define a function to print the solution board
def print_board(board):
    for row in board:
        print(row)

# Define the size of the chessboard
n = 8

# Initialize an empty chessboard
board = [[0 for _ in range(n)] for _ in range(n)]

# Solve the N-Queens problem using backtracking
if solve_nqueens(board, 0, n):
    print_board(board)
else:
    print("No solution exists.")

    
    
'''
This code defines three functions: can_place to check if a queen can be placed in a given cell, 
solve_nqueens to solve the N-Queens problem using backtracking, and print_board to print the solution board.
The chessboard is represented as a 2D list with 1s representing queens and 0s representing empty cells. 
The solve_nqueens function recursively places queens in each column of the chessboard and backtracks if no queen can be placed in a row.
The can_place function checks if a queen can be placed in a given cell by checking the row, column, and diagonal for other queens. 
The print_board function simply prints the solution board. The code initializes an empty chessboard of 
size n and solves the N-Queens problem using backtracking. If a solution exists, it prints the solution board. Otherwise, it prints "No solution exists."

'''
