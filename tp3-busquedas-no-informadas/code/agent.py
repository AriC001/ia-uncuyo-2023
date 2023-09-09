import random
from node import Node
class Agent:           
    def __init__(self,env): #recibe como parámetro un objeto de la clase 
        self.env = env
        self.start = env.grilla[env.start[0]][env.start[1]]
        self.goal = env.grilla[env.finish[0]][env.finish[1]]
        self.cost = 0
       
    def BFS(self):
        goal = False
        cola = []
        cola.append(self.start)
        self.start.visited = True
        while cola and not goal:
            nodo_actual = cola.pop(0)
            self.cost+=1
            # print(nodo_actual.childs)
            if nodo_actual.value == 3:
                goal = True
                break
                
            for hijos in nodo_actual.childs:
                if not hijos.visited:
                    hijos.parent = nodo_actual
                    hijos.visited = True
                    cola.append(hijos)
            # print(cola)
        return nodo_actual