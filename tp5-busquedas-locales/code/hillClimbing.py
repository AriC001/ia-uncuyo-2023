import board as Board
import copy
import random

def neighbor(board):
    states = 0
    keepGoing = True
    keepGoing2 = True
    while states < 1000 and keepGoing2 == True:
        for col in range(board.size):
            # print(col)
            filas = 0
            keepGoing = True
            while filas < board.size and keepGoing == True:
                if board.board[filas][col] == 1:
                    neighbor = copy.deepcopy(board)
                    neighbor.board[filas][col]=0
                    values = []
                    for movement in range(board.size):
                        states+=1

                        neighbor.board[movement][col]=1
                        # Board.Board.printear(neighbor)
                        # print("valor previo: ",neighbor.value)
                        Board.Board.h(neighbor)
                        # print("valor despues: ",neighbor.value)
                        values.append(neighbor.value)
                        neighbor.board[movement][col]=0
                    if min(values) < board.value:
                        pos = 0
                        positions = []
                        for value in values:
                            if value == min(values):
                                positions.append(pos)
                            pos+=1
                        if pos >= 1:
                            pos = random.randint(positions[0],positions[positions.__len__()-1])
                            # print(positions)
                            # print(pos)
                            neighbor.board[pos][col] = 1
                            board.board = neighbor.board
                            board.value = neighbor.value
                            keepGoing = False
                            if board.value == 0:
                                keepGoing2 = False
                    else:
                        keepGoing = False
                        if board.value == 0:
                            keepGoing = False
                        continue
                        # return board
                filas+=1
    return states, values


def neighbor2(board):
    states = 0
    keepGoing = True
    keepGoing2 = True
    values2 = []
    values2.append(board.value)
    while states < 1000 and keepGoing2 == True:
        for col in range(board.size):
            keepGoing = True
            for filas in range(board.size):
                if keepGoing:
                    if board.board[filas][col] == 1:
                        neighbor = copy.deepcopy(board)
                        neighbor.board[filas][col]=0
                        values = []
                        for movement in range(board.size):
                            states+=1

                            neighbor.board[movement][col]=1
                            # Board.Board.printear(neighbor)
                            # print("valor previo: ",neighbor.value)
                            Board.Board.h(neighbor)
                            # print("valor despues: ",neighbor.value)
                            values.append(neighbor.value)
                            neighbor.board[movement][col]=0
                        if min(values) < board.value:
                            newList = [values2[-1]]*(states - len(values2))
                            values2.extend(newList)
                            valor = min(values)
                            values2.append(valor)
                            pos = 0
                            positions = []
                            for value in values:
                                if value == min(values):
                                    positions.append(pos)
                                pos+=1
                            if pos >= 1:
                                pos = random.randint(positions[0],positions[positions.__len__()-1])
                                # print(positions)
                                # print(pos)
                                neighbor.board[pos][col] = 1
                                board.board = neighbor.board
                                board.value = neighbor.value
                                keepGoing = False
                                if board.value == 0:
                                    keepGoing2 = False
                        else:
                            keepGoing = False
                            if board.value == 0:
                                keepGoing2 = False
                            # return board
                        # values2 += values
    return states, values2


def neighbor3(board):
    states = 0
    keepGoing2 = True
    values2 = [board.value]  # Inicializa values2 con el valor inicial
    last_added_state = 0  # Seguimiento del último estado en el que se agregó un valor

    while states < 1000 and keepGoing2:
        for col in range(board.size):
            keepGoing = True
            for filas in range(board.size):
                if keepGoing:
                    if board.board[filas][col] == 1:
                        neighbor = copy.deepcopy(board)
                        neighbor.board[filas][col] = 0
                        values = []
                        for movement in range(board.size):
                            states += 1
                            neighbor.board[movement][col] = 1
                            Board.Board.h(neighbor)
                            values.append(neighbor.value)
                            neighbor.board[movement][col] = 0
                        if min(values) < board.value:
                            valor = min(values)
                            # Repite el último valor antes de agregar el nuevo valor mínimo
                            values2.extend([values2[-1]] * (states - last_added_state - 1))
                            values2.append(valor)  # Agrega el nuevo valor
                            last_added_state = states  # Actualiza el último estado
                            pos = 0
                            positions = []
                            for value in values:
                                if value == min(values):
                                    positions.append(pos)
                                pos += 1
                            if pos >= 1:
                                pos = random.randint(positions[0], positions[-1])
                                neighbor.board[pos][col] = 1
                                board.board = neighbor.board
                                board.value = neighbor.value
                                keepGoing = False
                                if board.value == 0:
                                    keepGoing2 = False
                        else:
                            keepGoing = False
                            if board.value == 0:
                                keepGoing2 = False

    # Asegurémonos de que values2 tenga la misma longitud que states
    while len(values2) < states:
        values2.append(values2[-1])

    return states, values2
