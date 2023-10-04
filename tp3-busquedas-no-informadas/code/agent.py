import random
from node import Node
class Agent:           
    def __init__(self,env,name): #recibe como parámetro un objeto de la clase 
        self.env = env
        self.start = env.grilla[env.start[0]][env.start[1]]
        self.goal = env.grilla[env.finish[0]][env.finish[1]]
        self.state = 0
        self.cost = 0
        self.name = name
        self.solutionFound = False
       
    def BFS2(self):
        goal = False
        # cola = []
        cola = [self.start]
        self.start.visited = True
        while cola and not goal:
            self.addstate()
            nodo_actual = cola.pop(0)
            # print(nodo_actual.childs)
            if nodo_actual.value == 3:
                goal = True
                return nodo_actual
                
            for hijos in nodo_actual.childs:
                if not hijos.visited:
                    # hijos.parent = nodo_actual
                    hijos.visited = True
                    hijos.parent = nodo_actual
                    # new_path = path + [hijos]  # Create a new path by appending the child node
                    # cola_element = (hijos, new_path) 
                    cola.append(hijos)
            # print(cola)
        return None
    
    def BFS(self):
        node = self.BFS2()
        if node is not None:
            self.path(node)
            self.solutionFound = True
            return self.state
        else:
            self.state = None
            return self.state
    
    def generateRoadDFS(self, start_node): 
        node = self.generateRoadDFS2(start_node)
        if node is not None:
            self.path(node)
            self.solutionFound = True
            return self.state
        else:
            self.state = None
            return self.state

    def generateRoadDFS2(self, start_node):             
        visited = set()
        stack = [start_node]
        while stack:
            self.addstate()
            node = stack.pop(0)
            # print(node)
            visited.add(node) 

            if node == self.goal:  # Supongamos que self.target_node es el nodo objetivo que busca DFS
                return node

            for childs in node.childs:
                if childs not in visited and not childs.visited:
                    childs.visited = True
                    childs.parent = node
                    # new_path = path + [childs]  # Create a new path by appending the child node
                    # stack_element = (childs, new_path)  # Create a tuple containing the child node and the new path
                    stack.insert(0,childs)  # Add the tuple to the stack for further exploration


        return None  # Si no se encuentra el objetivo, retorna una lista vacía
    
    def limitDFS(self,start_node,limit):
        if limit is not None:
            node = self.limitDFS2(start_node,limit)
            if node is not None:
                self.path(node)
                self.solutionFound = True
                return self.state
            else:
                self.state = None
                return self.state
        else:
            self.state = None
            return self.state
        
    def limitDFS2(self,start_node,limit):
        visited = set()
        stack = [start_node]
        while stack and limit != 0:
            self.addstate()
            limit-=1
            node = stack.pop(0)
            # print(node)
            visited.add(node) 

            if node == self.goal:  # Supongamos que self.target_node es el nodo objetivo que busca DFS
                return node

            for childs in node.childs:
                if childs not in visited and not childs.visited:
                    childs.visited = True
                    childs.parent = node
                    # new_path = path + [childs]  # Create a new path by appending the child node
                    # stack_element = (childs, new_path)  # Create a tuple containing the child node and the new path
                    stack.insert(0,childs)  # Add the tuple to the stack for further exploration


        return None  # Si no se encuentra el objetivo, retorna una lista vacía

    def path(self,node):
        path = []
        while node is not None:
            path.insert(0,node)
            # if node == self.start:
            #     print("hola")
            node = node.parent
        self.cost = path.__len__()


    def addstate(self):
        self.state+=1
