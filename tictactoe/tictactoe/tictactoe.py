"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count += 1
    if count % 2 == 0 or board == initial_state():
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid Action")

    board2 = copy.deepcopy(board)
    board2[action[0]][action[1]] = player(board)

    return board2


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # horizontally
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == O:
                return O
            elif board[i][0] == X:
                return X
            return None

    # vertically
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == O:
                return O
            elif board[0][j] == X:
                return X
            return None

    # diagonally top left
    for i in range(3):
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == O:
                return O
            elif board[0][0] == X:
                return X
            return None

    # diagonally top right
    for i in range(3):
        if board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] == O:
                return O
            elif board[0][2] == X:
                return X
            return None

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    elif winner(board) == O:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0  # tie


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    Minimum = float("inf")
    Maximum = float("-inf")

    if player(board) == X:
        return Max_Value(board, Maximum, Minimum)[1]
    return Min_Value(board, Maximum, Minimum)[1]


def Max_Value(board, Maximum, Minimum):
    move = None
    if terminal(board):
        return [utility(board), None]
    b = float('-inf')
    for action in actions(board):
        poss = Min_Value(result(board, action), Maximum, Minimum)[0]
        Maximum = max(Maximum, poss)
        if poss > b:
            b = poss
            move = action
        if Maximum >= Minimum:
            break
    return [b, move]


def Min_Value(board, Maximum, Minimum):
    move = None
    if terminal(board):
        return [utility(board), None]
    b = float('inf')
    for action in actions(board):
        poss = Max_Value(result(board, action), Maximum, Minimum)[0]
        Minimum = min(Minimum, poss)
        if poss < b:
            b = poss
            move = action
        if Maximum >= Minimum:
            break
    return [b, move]
