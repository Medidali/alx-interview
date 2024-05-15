#!/usr/bin/python3
"""N Queens problem solver"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col):
    """
    Utility function to solve N Queens problem recursively
    """
    # Base case: If all queens are placed then return true
    if col >= len(board):
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_n_queens_util(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution then backtrack
            board[i][col] = 0

    # If the queen can not be placed in any row in this column col, then return false
    return False


def solve_n_queens(N):
    """
    Solve the N Queens problem for a given N
    """
    # Initialize the board
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Start from the first column
    if not solve_n_queens_util(board, 0):
        print("No solution exists")
        return

    # Print all possible solutions
    for row in board:
        queen_positions = [[r, c] for c, r in enumerate(row)]
        print(queen_positions)


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the board size N
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queens(N)
