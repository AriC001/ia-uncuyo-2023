import board as Board
import copy
import random

def neighbor(board):
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
                    if pos > 1:
                        pos = random.randint(positions[0],positions[positions.__len__()-1])
                        # print(positions)
                        # print(pos)
                        neighbor.board[pos][col] = 1
                        board.board = neighbor.board
                        board.value = neighbor.value
                        keepGoing = False
                else:
                    keepGoing = False
                    continue
                    # return board
            filas+=1
    return



