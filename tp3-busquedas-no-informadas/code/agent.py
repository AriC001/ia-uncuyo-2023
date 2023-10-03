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
        # cola = []
        cola = [self.start]
        self.start.visited = True
        while cola and not goal:
            self.addCost()
            nodo_actual = cola.pop(0)
            # print(nodo_actual.childs)
            if nodo_actual.value == 3:
                goal = True
                return []
                
            for hijos in nodo_actual.childs:
                if not hijos.visited:
                    # hijos.parent = nodo_actual
                    hijos.visited = True
                    # new_path = path + [hijos]  # Create a new path by appending the child node
                    # cola_element = (hijos, new_path) 
                    cola.append(hijos)
            # print(cola)
        return []

    def generateRoadDFS(self, start_node):
        # print(start_node)                        
        visited = set()
        # stack = []
        # stack.insert(0,start_node)
        stack = [start_node]
        # while stack:
        #     self.addCost()
        #     node, path = stack.pop()
        #     visited.add(node)
        while stack:
            self.addCost()
            # temp = stack.pop()
            # node = temp
            # path = temp
            node = stack.pop(0)
            visited.add(node) 


            if node == self.goal:  # Supongamos que self.target_node es el nodo objetivo que busca DFS
                return []

            for childs in node.childs:
                if childs not in visited and not childs.visited:
                    childs.visited = True
                    # new_path = path + [childs]  # Create a new path by appending the child node
                    # stack_element = (childs, new_path)  # Create a tuple containing the child node and the new path
                    stack.insert(0,childs)  # Add the tuple to the stack for further exploration


        return []  # Si no se encuentra el objetivo, retorna una lista vacía


    def addCost(self):
        self.cost+=1
