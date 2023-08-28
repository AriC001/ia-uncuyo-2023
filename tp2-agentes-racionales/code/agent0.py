import random
class Agent:           
    def __init__(self,env): #recibe como parámetro un objeto de la clase 
        self.env = env
        self.points = 0
        self.remaining_moves = 1000

    def up(self):
        if(self.env.accept_action("Arriba")== True):
            # self.points += 1
            self.remaining_moves =  self.remaining_moves - 1
    def down(self):
        if(self.env.accept_action("Abajo") == True):
            # self.points += 1
            self.remaining_moves =  self.remaining_moves - 1
    def left(self):
        if(self.env.accept_action("Izquierda")== True):
            # self.points += 1
            self.remaining_moves =  self.remaining_moves - 1
    def right(self):
        if(self.env.accept_action("Derecha")== True):
            # self.points += 1
            self.remaining_moves =  self.remaining_moves - 1
    def suck(self): # Limpia
        if(self.env.accept_action("Limpiar") == True):
            self.points += 1
            self.remaining_moves =  self.remaining_moves - 1
    def idle(self): # no hace nada
        self.remaining_moves =  self.remaining_moves - 1
        return 0
    
    def perspective(self): #sensa el entorno
        if(self.env.is_dirty()==1):
            self.suck()
        else:
            match random.randint(0,4):
                case 0:
                    self.up()
                case 1:
                    self.down()
                case 2:
                    self.left()
                case 3:
                    self.right()
                case 4:
                    self.idle()

    def think(self): # implementa las acciones a seguir por el agente
        match random.randint(0,5):
            case 0:
                self.up()
            case 1:
                self.down()
            case 2:
                self.left()
            case 3:
                self.right()
            case 4:
                self.suck()
            case 5:
                self.idle()
    
    def reset(self):
        self.points = 0
        self.remaining_moves = 1000