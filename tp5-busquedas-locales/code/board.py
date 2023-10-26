import random
import hillClimbing as HillC
import simulatedAnnealing as SmAn
import genetic as Gen
import utils
class Board:
    def __init__(self, queens):
        self.size = queens
        self.queens = queens
        self.value = 1
        self.values = []
        self.statesHill = 0
        self.statesAnn = 0
        self.statesGen = 0
        self.board = []
        self.makeBoard()
        self.h()



    def makeBoard(self):
        self.board = [[0 for filas in range(self.size)] for col in range(self.size)]
        states = list(range(self.queens))
        for i in range(self.size):
            elemento_aleatorio = random.choice(states)
            self.board[elemento_aleatorio][i] = 1
            states.remove(elemento_aleatorio)

        # cont = 0
        # while cont != self.size:
        #     i,j = random.sample(range(self.size),2)
        #     if self.board[i][j] == 0:
        #         self.board[i][j] = 1
        #         cont+=1
        return

    def h(self):
        collision = 0

        # Para colisiones en la misma fila
        collision_in_row = 0
        queens_in_row = 0
        for filas in range(self.size):
            for col in range(self.size):
                # if col == 0:
                #     if queens_in_row > 1:
                #         collision_in_row += queens_in_row
                #     queens_in_row = 0
                if self.board[filas][col] == 1:
                    columnas = col+1
                    while columnas < self.size:
                        if self.board[filas][columnas] == 1:
                            queens_in_row+=1
                        columnas+=1

        collision_in_row = queens_in_row
        

        collision_in_col = 0
        queens_in_col = 0
        for col in range(self.size):
            for filas in range(self.size):
                # if filas == 0:
                #     if queens_in_col > 1:
                #         collision_in_col += queens_in_col
                #     queens_in_col = 0
                if self.board[filas][col] == 1:
                    filas2 = filas+1
                    while filas2 < self.size:
                        if self.board[filas2][col] == 1:
                            queens_in_col+=1
                        filas2+=1
        collision_in_col = queens_in_col

        # Para colisiones en las diagonales
        queens_in_diagonal = 0
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 1:
                    # Verifica las reinas en la misma diagonal hacia arriba y hacia la izquierda
                    r, c = row - 1, col - 1
                    while r >= 0 and c >= 0:
                        if self.board[r][c] == 1:
                            queens_in_diagonal += 1
                        r -= 1
                        c -= 1
                    
                    # Verifica las reinas en la misma diagonal hacia arriba y hacia la derecha
                    r, c = row - 1, col + 1
                    while r >= 0 and c < self.size:
                        if self.board[r][c] == 1:
                            queens_in_diagonal += 1
                        r -= 1
                        c += 1
        collision_in_diag = queens_in_diagonal
        # return queens_in_diagonal

        # # print(queens_in_diagonals)
        # for queens in queens_in_diagonals:
        #     if queens > 1:
        #         collision_in_diag += queens

        collision = collision_in_diag + collision_in_row + collision_in_col
        self.value = collision

        return
        
        # #para misma fila:
        # collision = 0
        # contQueens = 0
        # for filas in range(self.size):
        #     for col in range(self.size):
        #         if col == 0:
        #             if contQueens > 1:
        #                 collision += contQueens
        #             contQueens = 0
        #         if self.board[filas][col] == 1:
        #             contQueens+=1
        
        # ##
        # #para misma columna
        # for col in range(self.size):
        #     contQueens = 0
        #     for filas in range(self.size):
        #         if self.board[filas][col] == 1:
        #             contQueens += 1
        #     collision += max(0, contQueens - 1)  # Restar 1 para evitar contar la reina actual

        ##
        #para diagonal

        ##


        # 1 menos el collisiones/total, si hay 4 colisiones (la mitad de las reinas) => 1-(4/8) = 0.5            
        # self.value = 1-(self.size/collision)
        # return
    
    def crossJoin(self,board):
        return
    
    def hillClimbing(self,plot):
        self.statesHill,self.values = HillC.neighbor3(self)
        if self.queens == 12 and plot == True:
            print(self.statesHill)
            print(self.values.__len__())
            # print(self.statesHill)
            # print(self.values)
            # self.values.reverse()
            utils.plotFitness(self.values,"Hill Climbing")
        return
    
    def simulatedAnnealing(self,plot):
        self.statesAnn,self.values = SmAn.simulatedAnnealing(self)
        if self.queens == 12 and plot:
            # print(self.statesAnn)
            # print(self.values)
            # self.values.reverse()
            utils.plotFitness(self.values,"Simulated Annealing")
        return
    
    
    def genetic(self,plot):
        self.statesGen = Gen.genetic(self,plot)
        print(self.statesGen)
        # if self.queens == 12:
        #     self.values.reverse()
        #     utils.plotFitness(self.values,"Genetic")
        return
    
    # def simulatedAnnealing2(self):
    #     self,evaluations = SmAn.simulatedAnnealing2(self)
    #     # if evaluations < 10000:
    #         # print(evaluations)
    #     return
    
    def queensCount(self):
        count = 0
        for i in range(self.queens):
            for j in range(self.queens):
                if self.board[i][j] == 1:
                    count+=1
        return count
    
    def isValidSolution(self):
        if self.queensCount() == self.queens:
            return True
        else:
            return False

    def changeValue(self):
        self.value = 1
        

    def printear(self):
        for filas in range(self.size):
            for col in range(self.size):
                print(self.board[filas][col],end="")
            print()













    
    # def lowerValue(self, collision):
