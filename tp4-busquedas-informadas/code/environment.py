import random

class Environment:
    def __init__(self, n):
        self.statesExplored = 0
        self.size = n
        self.row = n
        self.column = n
        self.start = self.generateStartFinish("start")
        self.finish = self.generateStartFinish("finish")
        self.grid = [[0 for _ in range(n)] for _ in range(n)]
        # self.start = None
        # self.finish = None
        self.grid = self.generateObstacles()

    def generateObstacles(self):
        for i in range(self.size):
            for j in range(self.size):
                if random.random() < 0.08:
                    self.grid[i][j] = 1
        return self.grid

    def generateStartFinish(self, type):
        if type == "start":
            start_i, start_j = random.randint(0, self.size-1), random.randint(0, self.size-1)
            self.start = (start_i, start_j)
            return (start_i, start_j)
        if type == "finish":
            while True:
                finish_i, finish_j = random.randint(0, self.size-1), random.randint(0, self.size-1)
                if (self.start[0], self.start[1]) != (finish_i, finish_j):
                    self.finish = (finish_i, finish_j)
                    return self.finish
                    break
    
    def performAction(self,state, action):
        x, y = state
        if action == "up":
            x -= 1
            if self.isValidLocation(x, y):
                return x , y
            else:
                return None
        elif action == "down":
            x += 1
            if self.isValidLocation(x, y):
                return x , y
            else:
                return None
        elif action == "left":
            y -= 1
            if self.isValidLocation(x, y):
                return x , y 
            else:
                return None
        elif action == "right":
            y += 1
            if self.isValidLocation(x, y):
                return x , y 
            else:
                return None

    def isValidLocation(self, x, y):
        return 0 <= x < self.row and 0 <= y < self.column and self.grid[x][y] != 1
