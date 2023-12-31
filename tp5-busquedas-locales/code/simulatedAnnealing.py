import math
import copy
import random
import board as Board

def simulatedAnnealing(board):
    temperature = 1000
    coolingRate = 0.97
    evaluations = 0
    maxEvaluations = 1000
    values = []
    keepGoing = True

    while evaluations < maxEvaluations and keepGoing == True:
        newBoard = Board.Board(board.size)
        newBoard = copy.deepcopy(board)
        i = random.randint(0,board.size-1)
        j = random.randint(0,board.size-1)
        temp = newBoard.board[i]
        newBoard.board[i] = newBoard.board[j]
        newBoard.board[j] = temp
        Board.Board.h(newBoard)
        values.append(newBoard.value)
        bool,temperature = acceptance_probability(board.value,newBoard.value,temperature,coolingRate)
        if bool==True:
            board.board = newBoard.board
            board.value = newBoard.value

        evaluations +=1
        if board.value == 0:
            keepGoing = False

    return evaluations,values



def simulatedAnnealing2(board):
    temperature = 1000
    coolingRate = 0.95
    evaluations = 0
    maxEvaluations = 10000
    keepGoing = True
    keepGoing2 = True
    keepGoing3 = True
    while evaluations < maxEvaluations:
            keepGoing2 = True
            keepGoing3 = True
            for col in range(board.size):
                for filas in range(board.size):
                    if keepGoing2:
                        if board.board[filas][col] == 1:
                            newBoard = copy.deepcopy(board)
                            newBoard.board[filas][col]=0
                            for movement in range(board.size):
                                if keepGoing3:
                                    if board.board[movement][col] != 1:
                                        newBoard.board[movement][col]=1
                                        Board.Board.h(newBoard)
                                        if acceptance_probability(board.value,newBoard.value,temperature,coolingRate) == True:
                                            board = copy.deepcopy(newBoard)
                                            newBoard.board[movement][col]=0
                                            keepGoing3 = False
                                            # keepGoing2 = False
                                        else:
                                            newBoard.board[movement][col]=0
                                            # keepGoing2 = False
                                            # keepGoing3 = False
                                        if(board.value == 0):
                                            keepGoing = False
                                            keepGoing2 = False
                                            keepGoing3 = False
                                            return board,evaluations
            evaluations+=1
            # print(evaluations)
    return board,evaluations


    while evaluations < maxEvaluations and keepGoing == True:
        for col in range(board.size):
            keepGoing = True
            # print(col)
            filas = 0
            while filas < board.size and keepGoing == True:
                # print("aa")
                if board.board[filas][col] == 1:
                    # print("bb")
                    newBoard = copy.deepcopy(board)
                    newBoard.board[filas][col]=0
                    values = []
                    # filas = board.size
                    for movement in range(board.size):
                        if board.board[movement][col] != 1:
                            # print("cc")
                            # newBoard = copy.deepcopy(board)
                            newBoard.board[movement][col]=1
                            # Board.Board.printear(neighbor)
                            # print("valor previo: ",neighbor.value)
                            Board.Board.h(newBoard)
                            # print("valor despues: ",neighbor.value)
                            # values.append(newBoard.value)
                            if acceptance_probability(board.value,newBoard.value,temperature,coolingRate) == True:
                                # print("dd")
                                newBoard.board[movement][col] = 1
                                board = copy.deepcopy(newBoard)
                                # board.board = newBoard.board
                                # board.value = newBoard.value
                                # keepGoing = False
                                newBoard.board[movement][col]=0
                            else:
                                newBoard.board[movement][col]=0
                                keepGoing = False
                                #inue
                                # return board
                            if(board.value == 0):
                                keepGoing=False
                                col = board.size
                filas+=1
            evaluations+=1
            print(evaluations,end=" ")
    return board,evaluations




def acceptance_probability(actual_value, proposed_value, temperature,coolingRate):
    if proposed_value < actual_value:
        temperature *= coolingRate
        return True,temperature  # Si el valor propuesto es mejor, se acepta de inmediato
    else:
        if(random.uniform(0,1) <= math.exp((actual_value - proposed_value) / temperature)):
            # print("aloja: ",math.exp((actual_value - proposed_value) / temperature),end="  ")
            temperature *= coolingRate
            return True,temperature
        else:
            temperature *= coolingRate
            return False,temperature
