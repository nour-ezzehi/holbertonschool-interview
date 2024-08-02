#!/usr/bin/python3
""" 0. N queens """
import sys


def is_not_safe_position(board, i, j, r):
    """ Determines if position (i, j) on the chessboard is safe
    to allocate a queen """

    if (board[i] == j) or (board[i] == j - i + r) or (board[i] == i - r + j):
        return True
    return False


def find_positions(board, row, n):
    """ Finds all safe position (i, j) where n queens
    can be allocated
    """
    if row == n:
        print_chess_board(board, n)

    else:
        for j in range(n):
            legal = True
            for i in range(row):
                if is_not_safe_position(board, i, j, row):
                    legal = False
            if legal:
                board[row] = j
                find_positions(board, row + 1, n)


def print_chess_board(board, n):
    """ generates the list of positions (i, j) where n queens
    were allocated
    """
    b = list()

    for i in range(n):
        for j in range(n):
            if j == board[i]:
                b.append([i, j])
    print(b)


def create_chess_board(size):
    """ generates a list of zeros """

    return [0 * size for i in range(size)]


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except BaseException:
    print("N must be a number")
    exit(1)

if (n < 4):
    print("N must be at least 4")
    exit(1)

board = create_chess_board(int(n))

row = 0
find_positions(board, row, int(n))
