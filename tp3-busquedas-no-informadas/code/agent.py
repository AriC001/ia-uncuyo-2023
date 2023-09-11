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

    def generateRoadDFS(self, start_node):
        visited = set()
        stack = [(start_node, [start_node])]

        while stack:
            self.addCost()
            node, path = stack.pop()
            visited.add(node)

            if node == self.goal:  # Supongamos que self.target_node es el nodo objetivo que busca DFS
                return path

            for neighbor in node.childs:
                if neighbor not in visited and not neighbor.visited:
                    neighbor.visited = True
                    stack.append((neighbor, path + [neighbor]))

        return []  # Si no se encuentra el objetivo, retorna una lista vacía


    def addCost(self):
        self.cost+=1
