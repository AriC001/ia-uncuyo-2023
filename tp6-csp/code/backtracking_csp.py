import board as Board
import random
import copy

def backtrackingInit(queens,statesRecorded):
    initial_states = list(range(1, queens + 1))
    boards = []

    for state in initial_states:
        board = Board.Board(queens)
        board.board.append(state)
        available_states = initial_states.copy()
        available_states.remove(state)
        statesRecorded+=1

        backtracking(queens, board, available_states, boards,statesRecorded)
    boards.sort(key=lambda board: board.value)
    return boards,statesRecorded

def backtracking(queens, board, available_states, boards,statesRecorded):
    if len(board.board) == queens:
        Board.Board.h(board)
        if board.value < 1:
            boards.append(copy.deepcopy(board))
        return

    for state in available_states:
        statesRecorded+=1
        new_board = copy.deepcopy(board)
        new_board.board.append(state)
        new_available_states = available_states.copy()
        new_available_states.remove(state)
        Board.Board.h(new_board)
        if new_board.value == 0:  # Comprobar inmediatamente
            backtracking(queens, new_board, new_available_states, boards,statesRecorded)
        # backtracking(queens, new_board, new_available_states, boards)

# def backtracking(queens, position, boards, available_states):
#     if position == 0:
#         for i in range(queens):
#             boards.append(Board.Board(queens))
#         makeBoardOne(boards, position, available_states,queens)
#     else:
#         backtracking(queens, position-1, boards, available_states)
#         makeBoardOne(boards, position, available_states,queens)
#         if position == queens-1:
#             for board in boards:
#                 Board.Board.h(board)
#             boards.sort(key=lambda board: board.value)
#         return boards

# def makeBoardOne(boards, position, available_states,queens):
#     for board in boards:
#         if available_states:
#             state = random.choice(available_states)
#             board.board.append(state)
#             available_states.remove(state)
#         else:
#             # Si no quedan estados disponibles, simplemente elige uno al azar
#             state = random.randint(1, queens)
#             board.board.append(state)




