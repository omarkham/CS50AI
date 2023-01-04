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
                count+=1
    if count%2==0:
        return X
    return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                moves.add((i,j))
    return moves

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid Action")
    
    board2 = copy.deepcopy(board)
    board2[action[0]][actions[1]] = player(board)

    return board2
            
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #horizontally
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == EMPTY:
                return None
            elif board[i][0] == X:
                return X
            return O

    #vertically
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == EMPTY:
                return None
            elif board[0][i] == X:
                return X
            return O

    #diagonally top left
    for i in range(3):
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == EMPTY:
                return None
            elif board[0][0]:
                return X
            return O

    #diagonally top right
    for i in range(3):
        if board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] == EMPTY:
                return None
            elif board[0][2] == X:
                return X
            return O

    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                win == False

    if winner(board) != None:
        win = True

    return win

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0 #tie

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    inf = float("inf")
    ninf = float("-inf")

    if player(board) == X:
        return Max_Value(board, ninf, inf)[1]
    return Min_Value(board, inf, ninf)[1]
  
def Max_Value(board, Maximum, Minimum):
    move = None
    if terminal(board):
        return [utility(board), None]
    v = float("-inf")
    for action in actions(board):
        poss = Min_Value(result(board, action), Maximum, Minimum)[0]
        Maximum = max(Maximum, poss)
        if poss > v:
            move = action
        if Maximum >= Minimum:
            break
    return [v, move];

def Min_Value(board, Maximum, Minimum):
    move = None
    if terminal(board):
        return [utility(board), None]
    v = float("inf")
    for action in actions(board):
        poss = Max_Value(result(board, action), Maximum, Minimum)[0]
        Minimum = min(Minimum, poss)
        if poss < v:
            v = poss
        if Maximum >= Minimum:
            break
    return [v, move];
