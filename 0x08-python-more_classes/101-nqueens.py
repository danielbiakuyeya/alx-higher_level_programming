#!/usr/bin/python3
"""
N-Queens backtracking program to print the coordinates of N queens
on an NxN grid such that they are all in non-attacking positions
"""


from sys import argv

if __name__ == "__main__":
    queens = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    board_size = int(argv[1])
    if board_size < 4:
        print("N must be at least 4")
        exit(1)

    for i in range(board_size):
        queens.append([i, None])

    def already_exists(col):
        """Check that a queen does not already exist in that column"""
        for row in range(board_size):
            if col == queens[row][1]:
                return True
        return False

    def reject(row, col):
        """Determines whether or not to reject the solution"""
        if already_exists(col):
            return False
        i = 0
        while i < row:
            if abs(queens[i][1] - col) == abs(i - row):
                return False
            i += 1
        return True

    def clear_queens(start_row):
        """Clears the queens' positions from the point of failure onwards"""
        for i in range(start_row, board_size):
            queens[i][1] = None

    def nqueens(row):
        """Recursive backtracking function to find the solution"""
        for col in range(board_size):
            clear_queens(row)
            if reject(row, col):
                queens[row][1] = col
                if row == board_size - 1:
                    print(queens)
                else:
                    nqueens(row + 1)

    """Start the recursive process at row 0"""
    nqueens(0)

