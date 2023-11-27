import random

import numpy as np
from matplotlib import pyplot as plt


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y


BOARD_SIZE = 8

MOVE_X = [2, 1, -1, -2, -2, -1, 1, 2]
MOVE_Y = [1, 2, 2, 1, -1, -2, -2, -1]


def within_board(board, x, y):
    n = len(board)
    return (x >= 0 and y >= 0) and (x < n and y < n)


def isempty(board, x, y):
    n = len(board)
    return (within_board(board, x, y)) and (board[x][y] < 0)


def getDegree(board, x, y):
    n = len(board)
    count = 0
    for i in range(n):
        if isempty(board, (x + MOVE_X[i]), (y + MOVE_Y[i])):
            count += 1
    return count


def nextMove(board, cell):
    n = len(board)
    min_deg_idx = -1
    c = 0
    min_deg = n + 1
    nx = 0
    ny = 0

    start = random.randint(0, 1000) % n
    for count in range(0, n):
        i = (start + count) % n
        nx = cell.x + MOVE_X[i]
        ny = cell.y + MOVE_Y[i]
        c = getDegree(board, nx, ny)
        if (isempty(board, nx, ny)) and c < min_deg:
            min_deg_idx = i
            min_deg = c

    if min_deg_idx == -1:
        return None

    nx = cell.x + MOVE_X[min_deg_idx]
    ny = cell.y + MOVE_Y[min_deg_idx]

    board[nx][ny] = board[cell.x][cell.y] + 1

    cell.x = nx
    cell.y = ny

    return cell


def print_board(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


def is_neighbour(x, y, xx, yy):
    for i in range(BOARD_SIZE):
        if ((x + MOVE_X[i]) == xx) and ((y + MOVE_Y[i]) == yy):
            return True
    return False


def find_tour(init_x, init_y):
    n = BOARD_SIZE
    board = [[-1 for i in range(n)] for i in range(n)]

    cell = Cell(init_x, init_y)
    board[init_x][init_y] = 1

    ret = None
    for i in range(n**2 - 1):
        ret = nextMove(board, cell)
        if ret == None:
            return False

    print_board(board)
    if is_neighbour(ret.x, ret.y, init_x, init_y):
        print("Closed tour")
    else:
        print("Open tour")
    reversed_board = board[::-1]
    plot_knights_tour(reversed_board)

    coordinates = connect_cells(reversed_board)
    plt.plot(coordinates[:, 1] + 0.5, coordinates[:, 0] + 0.5, "ro-")
    plt.show()
    return True


def plot_knights_tour(board):
    n = len(board)

    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(0, n, 1))
    ax.set_yticks(np.arange(0, n, 1))
    ax.set_xticklabels([str(i + 1) for i in range(n)])
    ax.set_yticklabels([str(i + 1) for i in range(n)])
    ax.set_xlabel("Column")
    ax.set_ylabel("Row")

    for i in range(n):
        for j in range(n):
            ax.text(
                j + 0.5,
                i + 0.5,
                str(board[i][j]),
                ha="center",
                va="center",
                fontsize=15,
                color="black",
            )

    for i in range(n + 1):
        for j in range(n + 1):
            if j + 1 < n + 1:
                plt.plot([j, j + 1], [i, i], "k-", lw=2)
            if i + 1 < n + 1:
                plt.plot([j, j], [i, i + 1], "k-", lw=2)

    ax.set_xlim(-0.5, n + 1 - 0.5)
    ax.set_ylim(-0.5, n + 1 - 0.5)


def connect_cells(board):
    n = len(board)

    flat_board = [cell for row in board for cell in row]
    sorted_order = sorted(enumerate(flat_board, start=1), key=lambda x: x[1])

    coordinates = np.array([divmod(cell[0] - 1, n) for cell in sorted_order])
    return coordinates


if __name__ == "__main__":
    while not find_tour(0, 0):
        pass
