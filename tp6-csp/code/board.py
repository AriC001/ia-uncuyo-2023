import random

class Board:
    def __init__(self, queens):
        self.size = queens
        self.queens = queens
        self.value = 1
        self.values = []
        self.boardsBack = 0
        self.boardsFowChan = 0
        # self.boards = 0
        self.board = []
        # self.makeBoard()
        # self.h()



    def makeBoard(self):
        self.board = [0 for col in range(self.size)]
        boards = list(range(self.queens))
        for i in range(self.size):
            posicion_aleatoria = random.choice(boards)
            self.board[i] = posicion_aleatoria
            boards.remove(posicion_aleatoria)

        # cont = 0
        # while cont != self.size:
        #     i,j = random.sample(range(self.size),2)
        #     if self.board[i][j] == 0:
        #         self.board[i][j] = 1
        #         cont+=1
        return

    # def h(self):
    #     collision = 0
    #     for i in range(self.size-1):
    #         for j in range(self.size):
    #             if i != j:
    #                 if abs(i - j) == abs(self.board[i] - self.board[j]):
    #                     collision += 1
    #     self.value = collision
    #     return

    def h(self):  # devuelve la cantidad de pares de reinas amenazadas
        value = 0
        for i in range(len(self.board)):
            for j in range(i + 1, len(self.board)):
                # chequea si hay reinas en la misma fila o en la misma diagonal
                if self.board[i] == self.board[j] or abs(self.board[i] - self.board[j]) == j - i:
                    value += 1
        self.value=value
              
    # def checkRow(self, x, y):
    #     return x == y

    # def queensCount(self):
    #     count = 0
    #     for i in range(self.queens):
    #         for j in range(self.queens):
    #             if self.board[i][j] == 1:
    #                 count+=1
    #     return count
    
    # def isValidSolution(self):
    #     if self.queensCount() == self.queens:
    #         return True
    #     else:
    #         return False

    def changeValue(self):
        self.value = 1
        

    def printear(self):
        print(self.board)
    
    def printing(self):
        for i in range(self.queens):
            for j in range(self.queens):
                if j+1 == self.board[i]:
                    print("1",end=" ")
                else:
                    print("0",end=" ")
            print("")













    
    # def lowerValue(self, collision):
