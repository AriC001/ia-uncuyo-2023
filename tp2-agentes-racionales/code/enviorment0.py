import random
class Environment:
    def __init__(self,dirt_rate,sizeX):
        self.sizeX = sizeX-1
        self.sizeY = sizeX-1
        self.posX = random.randint(0, self.sizeX)
        self.posY = random.randint(0, self.sizeX)
        self.dirt_rate = dirt_rate
        self.dirty_squares = 0
        self.total_dirt_squares = 0
        self.matrix = [[i for i in range(self.sizeX+1)] for j in range(self.sizeY+1)]
        self.initializeMatrix()

        self.generate_dirt()

    def initializeMatrix(self):
        for i in range(self.sizeX+1):
            for j in range(self.sizeX+1):
                self.matrix[i][j]=0

    def generate_dirt(self):
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                if random.random() < self.dirt_rate:
                    self.matrix[i][j] = 1
                    self.dirty_squares = self.dirty_squares + 1
                else:
                    self.matrix[i][j] = 0
        self.total_dirt_squares = self.dirty_squares                

    def accept_action(self,action):
        match action:
            case "Arriba":
                if self.posY < self.sizeY-1:
                    self.posY+=1
                    return True
            case "Abajo":
                if self.posY > 0:
                    self.posY= self.posY - 1
                    return True
            case "Izquierda":
                if self.posX > 0:
                    self.posX = self.posX - 1
                    return True
            case "Derecha":
                if self.posX < self.sizeX-1:
                    self.posX+=1
                    return True
            case "Limpiar":
                if self.is_dirty() == 1:
                    self.matrix[self.posX][self.posY] = 0
                    self.dirty_squares = self.dirty_squares - 1
                    return True
                else:
                    return False

    def is_dirty(self):
        # print(self.sizeX, self.posX, self.sizeY, self.posY)
        if self.matrix[self.posX][self.posY] == 1:
            return 1
        else: 
            return 0
    
    def print_environment(self):
        print(self.matrix)

         
