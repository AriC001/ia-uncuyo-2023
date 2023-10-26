import board as Board
import random
import copy
import utils

def crossover(parent1,parent2):
    cut = random.randint(1,parent1.size-1)
    child = Board.Board(parent1.size)
    child.board = parent2.board[:cut] + parent1.board[cut:]
    # child = manteinQueensCount(child)
    # while int(child.queensCount()) > int(child.size):
    #     i = random.randint(0,child.size-1)
    #     j = random.randint(0,child.size-1)
    #     if child.board[i][j] == 1:
    #         child.board[i][j] = 0
    # while int(child.queensCount()) < int(child.size):
    #     i = random.randint(0,child.size-1)
    #     j = random.randint(0,child.size-1)
    #     if child.board[i][j] == 0:
    #         child.board[i][j] = 1
    return child

def mutation(child):
    prob = random.random()
    if prob >= 0.0 and prob < 0.85: #pick 0
        # i = random.randint(0,child.size-1)
        # j = random.randint(0,child.size-1)
        # temp = child.board[i]
        # child.board[i] = child.board[j]
        # child.board[j] = temp
        # child.board[i][j] = 0 if child.board[i][j]==1 else 1
        # child = manteinQueensCount(child)
        return child
    elif prob >= 0.85 and prob < 0.97: #pick 1
        i = random.randint(0,child.size-1)
        j = random.randint(0,child.size-1)
        temp = child.board[i]
        child.board[i] = child.board[j]
        child.board[j] = temp
        # child.board[i][j] = 0 if child.board[i][j]==1 else 1
        # i2 = random.randint(0,child.size-1)
        # j2 = random.randint(0,child.size-1)
        # temp = child.board[i2]
        # child.board[i2] = child.board[j2]
        # child.board[j2] = temp
        # child.board[i2][j2] = 0 if child.board[i2][j2]==1 else 1
        # child = manteinQueensCount(child)
        return child
    elif prob >= 0.97 and prob <= 1: #pick 2
        i = random.randint(0,child.size-1)
        j = random.randint(0,child.size-1)
        temp = child.board[i]
        child.board[i] = child.board[j]
        child.board[j] = temp
        # child.board[i][j] = 0 if child.board[i][j]==1 else 1
        i2 = random.randint(0,child.size-1)
        j2 = random.randint(0,child.size-1)
        temp = child.board[i2]
        child.board[i2] = child.board[j2]
        child.board[j2] = temp
        # child.board[i2][j2] = 0 if child.board[i2][j2]==1 else 1
        # i3 = random.randint(0,child.size-1)
        # j3 = random.randint(0,child.size-1)
        # temp = child.board[i3]
        # child.board[i3] = child.board[j3]
        # child.board[j3] = temp
        # child.board[i3][j3] = 0 if child.board[i3][j3]==1 else 1
        # child = manteinQueensCount(child)
        return child
    return child


def genetic(board,plot):
    population = []
    populationSize = 100
    maxIterations = 1000
    iterataion = 0
    values = []
    values.append(board.value)
    keepGoing = True

    for i in range(populationSize):
        population.append(Board.Board(board.size))
    
    while iterataion < maxIterations and keepGoing:
        population = sorted(population, key=lambda board: board.value, reverse=False)
        newList = [values[values.__len__()-1]]*(iterataion-1-values.__len__())
        values+=newList
        values.append(population[0].value)

        if min(values) == 0:
            keepGoing = False
            
            board.board = population[0].board
            board.value = population[0].value
            if plot:
                utils.plotFitness(values,"Genetic")
            return iterataion
        
        newPopulation = []
        probabilidades = []
        # population = sorted(population, key=lambda board: board.value, reverse=False)

        for i in range(int(populationSize/2)):
            probabilidades.append(population[i].value)
        
        # Normaliza las probabilidades
        total_probabilidades = sum(probabilidades) #if sum(probabilidades) != 0 else 1
        probabilidades_normalizadas = [p / total_probabilidades for p in probabilidades]
        probabilidades_invertidas = [1 - prob for prob in probabilidades_normalizadas]
                                     
        for i in range(populationSize):
            parent1 = random.choices(population[:int(populationSize/2)], weights = probabilidades_invertidas,k=1)[0]
            parent2 = random.choices(population[:int(populationSize/2)], weights = probabilidades_invertidas,k=1)[0]
            while parent1 == parent2:
                parent2 = random.choices(population[:int(populationSize/2)], weights = probabilidades_invertidas,k=1)[0]
            child = crossover(parent1,parent2)
            child = mutation(child)
            Board.Board.h(child)
            newPopulation.append(child)
        
        population = newPopulation
        iterataion += 1

    
    board.board = population[0].board
    board.value = population[0].value
    if plot:
        utils.plotFitness(values,"Genetic")
    return iterataion