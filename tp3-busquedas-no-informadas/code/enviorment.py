import random
from node import Node
class Environment:
    def __init__(self):
        self.sizeX = 100
        self.sizeY = 100
        self.grilla = [[0 for i in range(self.sizeX)] for j in range(self.sizeY)]
        self.start = (random.randint(0,99),random.randint(0,99))
        self.finish = (0,0)
        self.initializeMatrix()
        self.generteObst()
        
    def generteObst(self):
        for k in range(self.sizeX*self.sizeY):
            if random.random() <= 0.08:
                i = random.randint(0,99)
                j = random.randint(0,99)
                while (i == self.start[0] and j == self.start[1]) or (i == self.finish[0] and j == self.finish[1]):
                    i = random.randint(0,99)
                    j = random.randint(0,99)
                self.grilla[i][j]=1

    def initializeMatrix(self):
        self.finish = (random.randint(0,99),random.randint(0,99))
        while self.finish == self.start:
            self.finish = (random.randint(0,99),random.randint(0,99))
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                if i == self.finish[0] and j == self.finish[1]:
                    #  self.finish = self.grilla[i][j]
                     self.grilla[i][j] = 3
                elif i == self.start[0] and j == self.start[1]:
                    # self.start = self.grilla[i][j]
                    self.grilla[i][j] = 2
                else:
                    self.grilla[i][j]=0

    def generateRoad(self,node):
        road = []
        while node:
            road.append(node)
            node = node.parent
        return road
    
    def printear(self):
        for i in range(self.sizeX):
            print()
            for j in range(self.sizeY):
                print(self.grilla[i][j],end="")

    def visit(self):
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                self.grilla[i][j].visited = False
    