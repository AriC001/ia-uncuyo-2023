# from enviorment import Environment
import random

class Node:
    def __init__(self):
        # self.env = env
        self.value = 0
        self.parent = None
        self.visited = False
        # self.grilla = env.grilla
        # self.start = (env.start[0],env.start[1])
        self.childs = []
        # self.childsDown = []
        #     "arriba": None,
        #     "abajo": None,
        #     "izquierda": None,
        #     "derecha": None
        # }
        # self.grillaNode(env)
        # self.grillaNodeObst(env)
        self.i = 0
        self.j = 0


    # def setPosition(self,fila,columna):
    #     self.i = fila
    #     self.j = columna

def grillaNode(self,env,fila,columna):
    # for fila in range(env.sizeX):
    #     for columna in range(env.sizeY):
    self.i = fila
    self.j = columna
    self.value = env.grilla[fila][columna]
    env.grilla[fila][columna] = self
            # print(env.grilla[fila][columna])

def grillaNodeObst(env,fila,columna):
    # for fila in range(env.sizeX):
    #     for columna in range(env.sizeY):
    if env.grilla[fila][columna].value != 1:
        # if fila > 0:
        #     if env.grilla[fila - 1][columna].value != 1:
        #         # self.childs.append( env.grilla[fila - 1][columna])
        #         env.grilla[fila][columna].childs.append(env.grilla[fila - 1][columna])
        #         env.grilla[fila][columna].childsDown.append(env.grilla[fila - 1][columna])
        if fila < env.sizeX - 1:
            if env.grilla[fila + 1][columna].value != 1:
                # self.childs.append(env.grilla[fila + 1][columna])
                env.grilla[fila][columna].childs.append(env.grilla[fila + 1][columna])
            if columna < env.sizeY - 1:
                if env.grilla[fila + 1][columna + 1].value != 1:
                    # self.childs.append(env.grilla[fila + 1][columna])
                    env.grilla[fila][columna].childs.append(env.grilla[fila + 1][columna + 1])
            if columna > 0:
                if env.grilla[fila + 1][columna - 1].value != 1:
                    # self.childs.append(env.grilla[fila + 1][columna])
                    env.grilla[fila][columna].childs.append(env.grilla[fila + 1][columna - 1])

            # if env.grilla[fila + 1][columna].value != 1:
        # if columna > 0:
        #     if env.grilla[fila][columna - 1].value != 1:
        #         # self.childs.append( env.grilla[fila][columna - 1])
        #         env.grilla[fila][columna].childs.append(env.grilla[fila][columna - 1])
        # if columna < env.sizeY - 1:
        #     if env.grilla[fila][columna + 1].value != 1:
        #         # self.childs.append(env.grilla[fila][columna + 1])
        #         env.grilla[fila][columna].childs.append(env.grilla[fila][columna + 1])

def nodificar(env):
    for i in range(100):
        for j in range(100):
            nodo = Node()
            grillaNode(nodo,env,i,j)

    for i in range(100):
        for j in range(100):
            grillaNodeObst(env,i,j)

def printear(env):
    for i in range(100):
        for j in range(100):
            env.grilla[i][j].visited = False
