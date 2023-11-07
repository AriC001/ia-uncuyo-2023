import board as Board
import random
import copy

def forwardCheckingInit(queens,statesRecorded):
    initial_states = list(range(1, queens + 1))
    boards = []

    # print(boardStates)
    for state in initial_states:
        statesRecorded+=1
        board = Board.Board(queens)
        board.board.append(state)

        boardStates = []
        for _ in range(queens):
            boardStates.append(list(initial_states))

        # Realizar una copia profunda de boardStates para evitar compartir sublistas
        boardStatesCopy = [list(sublist) for sublist in boardStates]
        
        # Eliminar el estado que acabas de agregar de la lista de estados disponibles en todas las posiciones de boardStates
        removeInvalidStates(boardStatesCopy, state)
        # removeInvalidStates(boardStates, state)
        # print(boardStates)
        # available_states = initial_states.copy()
        # available_states.remove(state)

        forwardChecking(queens, board, boardStatesCopy, boards,statesRecorded)
    # boards.sort(key=lambda board: board.value)
    # print(boards)
    if len(boards) == 0:
        boards,statesRecorded = forwardCheckingInit(queens,statesRecorded)
    return boards,statesRecorded

def forwardChecking(queens, board, boardStates, boards,statesRecorded):
    if len(board.board) == queens:
        Board.Board.h(board)
        if board.value < 1:
            boards.append(copy.deepcopy(board))
        return
    
    position = len(board.board)
    # Realizar una copia profunda de boardStates
    boardStatesCopy = copy.deepcopy(boardStates)
    boardStatesCopy = possibleLegalStates(queens, board, boardStatesCopy)
    if boardStatesCopy == 0:
        return
    # print(boardStates)
    # print(position)
    # print(boardStates[position])
    state = random.choice(boardStatesCopy[position])
    board.board.append(state)
    removeInvalidStates(boardStatesCopy, state)
    forwardChecking(queens, board, boardStatesCopy, boards,statesRecorded)
    statesRecorded+=1
    return 

def possibleLegalStates(queens, board, boardStates):
    i = len(board.board)-1
    inputState = board.board[len(board.board)-1]

    # print("AA ",inputState)
    # print(boardStates)
    sumador = 1
    restador = -1
    for j in range(i+1,len(boardStates)):
        boardStatesCopy = copy.deepcopy(boardStates[j])
        if boardStatesCopy.count(inputState+sumador) > 0:
            boardStatesCopy.remove(inputState+sumador)
        if boardStatesCopy.count(inputState+restador) > 0:
            boardStatesCopy.remove(inputState+restador)
        boardStates[j] = []
        boardStates[j] = boardStatesCopy
        # print("BB ",boardStates[j])
        # print("CC ",boardStates)
        if len(boardStates[j]) == 0:
            # print("DD ",boardStates)
            # print(board.board)
            return 0
        sumador += 1
        restador -= 1
    # for
    #     posibleState = random.choice(boardStates[j])
    #     new_board = copy.deepcopy(board)
    #     new_board.board.append(posibleState)
    #     Board.Board.h(new_board)
    #     if new_board.value != 0:
    #         boardStates[j].remove(posibleState)
    return boardStates

def removeInvalidStates(boardStates, state):
    for i in range(len(boardStates)):
        available_states = boardStates[i]
        if state in available_states:
            available_states.remove(state)
        boardStates[i] = available_states