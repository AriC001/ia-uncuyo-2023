import random
import hillClimbing as HillC
class Board:
    def __init__(self, queens):
        self.size = queens
        self.value = 1
        self.board = []
        self.makeBoard()
        self.h()



    def makeBoard(self):
        self.board = [[0 for filas in range(self.size)] for col in range(self.size)]
        for i in range(self.size):
            self.board[0][i] = 1
        return

    def h(self):
        collision = 0

        # Para colisiones en la misma fila
        collision_in_row = 0
        queens_in_row = 0
        for filas in range(self.size):
            for col in range(self.size):
                if col == 0:
                    if queens_in_row > 1:
                        collision_in_row += queens_in_row
                    queens_in_row = 0
                if self.board[filas][col] == 1:
                    queens_in_row+=1
        # print(collision_in_row) 
        

        collision_in_col = 0
        queens_in_col = 0
        for col in range(self.size):
            for filas in range(self.size):
                if filas == 0:
                    if queens_in_col > 1:
                        collision_in_col += queens_in_col
                    queens_in_col = 0
                if self.board[filas][col] == 1:
                    queens_in_col+=1
        # print(collision_in_col) 

        # Para colisiones en las diagonales
        collision_in_diag = 0
        queens_in_diagonals = []
    
        for k in range(1 - self.size, self.size):
            # Recorre las diagonales desde la izquierda hacia la derecha
            diagonal = [self.board[i][i + k] for i in range(max(0, -k), min(self.size, self.size - k))]
            queens_in_diagonals.append(diagonal.count(1))
            
            # Recorre las diagonales desde la derecha hacia la izquierda
            diagonal = [self.board[i][self.size - 1 - i - k] for i in range(max(0, -k), min(self.size, self.size - k))]
            queens_in_diagonals.append(diagonal.count(1))
        
        # print(queens_in_diagonals)
        for queens in queens_in_diagonals:
            if queens > 1:
                collision_in_diag += queens


        collision = collision_in_diag + collision_in_row + collision_in_col
        collision = 8 if collision>8 else collision
        self.value = 1-(self.size/collision)

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
    
    def hillClimbing(self,board):
        #HillC.algo(self)
        return
    
    def changeValue(self):
        self.value = 1
        

    def printear(self):
        for filas in range(self.size):
            for col in range(self.size):
                print(self.board[filas][col],end="")
            print()













    
    # def lowerValue(self, collision):
