#!/usr/bin/python3

import sys

def solve(n):
    """Solves the N-Queens problem and returns all possible solutions."""
    solutions = [[]]
    for row in range(n):
        solutions = place_queen(row, n, solutions)
    return solutions

def place_queen(row, n, previous_solutions):
    """Places a queen in a given row and generates new solutions."""
    new_solutions = []
    for solution in previous_solutions:
        for col in range(n):
            if is_safe(row, col, solution):
                new_solutions.append(solution + [col])
    return new_solutions

def is_safe(row, col, solution):
    """Checks if a queen can be placed at (row, col) without being attacked."""
    for r in range(row):
        if solution[r] == col or abs(solution[r] - col) == row - r:
            return False
    return True

def init():
    """Initializes the program by parsing the command line arguments."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    return n

def n_queens():
    """Main function to solve the N-Queens problem and print solutions."""
    n = init()
    solutions = solve(n)
    for solution in solutions:
        print([[row, col] for row, col in enumerate(solution)])

if __name__ == '__main__':
    n_queens()

