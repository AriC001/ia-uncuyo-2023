import multiprocessing
import board as Board
import time
import csv
from random import sample
import math
import utils


def runner(queens,results):
    #
    solutionFondHillClimb = 0
    statesHillClimb = []
    statesHillClimbProm = 0
    duration_hillClimbing = []
    AVG_duration_hillClimbing = 0
    std_duration_hillClimbing = 0
    #
    solutionFondSimulatedAn = 0
    statesSimulatedAn = []
    statesSimulatedAnProm = 0
    duration_SimulatedAn = []
    AVG_duration_SimulatedAn = 0
    std_duration_SimulatedAn = 0
    #
    solutionFondGenetic = 0
    statesGenetic = []
    statesGeneticProm = 0
    duration_genetic = []
    AVG_duration_genetic = 0
    std_duration_genetic = 0
    for j in range(30): # Creacion de tableros con n queens

        ## Hill
        tableros = []
        for i in range(queens):
            board = Board.Board(queens)
            tableros.append(board)

        tableros = sorted(tableros, key=lambda board: board.value, reverse=False)
        start_time_hillClimbing = time.time()

        for i in range(1):
            if j == 29:
                tableros[i].hillClimbing(True)
            else:
                tableros[i].hillClimbing(False)
            statesHillClimb.insert(0,tableros[i].statesHill)
        tableros = sorted(tableros, key=lambda board: board.value, reverse=False)
        duration_hillClimbing.insert(0,time.time() - start_time_hillClimbing)
        AVG_duration_hillClimbing += duration_hillClimbing[0]
        tableros = sorted(tableros, key=lambda board: board.value, reverse=False)
        statesHillClimbProm += statesHillClimb[0]
        
        if tableros[0].value == 0:
            solutionFondHillClimb+=1


        ## SimAnn
        tableros = []
        for i in range(queens):
            board = Board.Board(queens)
            tableros.append(board)

        start_time_SimulatedAn = time.time()
        for i in range(1):
            if j == 29:
                tableros[i].simulatedAnnealing(True)
            else:
                tableros[i].simulatedAnnealing(False)
            statesSimulatedAn.insert(0, tableros[i].statesAnn)
        tableros = sorted(tableros, key=lambda board: board.value, reverse=False)
        duration_SimulatedAn.insert(0,time.time() - start_time_SimulatedAn)
        statesSimulatedAnProm += statesSimulatedAn[0]
        AVG_duration_SimulatedAn += duration_SimulatedAn[0]
        
        if tableros[0].value == 0:
            solutionFondSimulatedAn+=1


        ## GEN
        tableros = []
        for i in range(1):
            board = Board.Board(queens)
            tableros.append(board)
        
        start_time_gen = time.time()
        for i in range(1):
            if j == 1 and queens == 12:
                tableros[i].genetic(True)
            else:
                tableros[i].genetic(False)
            statesGenetic.insert(0, tableros[i].statesGen)
        tableros = sorted(tableros, key=lambda board: board.value, reverse=False)
        duration_genetic.insert(0,time.time() - start_time_gen)

        statesGeneticProm += statesGenetic[0]
        AVG_duration_genetic += duration_genetic[0]
        
        if tableros[0].value == 0:
            solutionFondGenetic+=1
        
    std_duration_hillClimbing = utils.standDev(duration_hillClimbing,AVG_duration_hillClimbing)
    std_duration_SimulatedAn = utils.standDev(duration_SimulatedAn,AVG_duration_SimulatedAn)
    std_duration_genetic = utils.standDev(duration_genetic,AVG_duration_genetic)
    stdStatesHill = utils.standDev(statesHillClimb,statesHillClimbProm/30)
    stdStatesSmAnn = utils.standDev(statesSimulatedAn,statesSimulatedAnProm/30)
    stdStatesGen = utils.standDev(statesGenetic,statesGeneticProm/30)
    if queens == 12:
        utils.plotTimes(duration_hillClimbing,duration_SimulatedAn,duration_genetic)
    results.append({"Tamaño Tablero": queens, "Algoritmo": "Hill Climbing", "Porcentaje de Exito": str((solutionFondHillClimb/30)*100)+"%", "Avg Execution Time": AVG_duration_hillClimbing/30 , "Std Execution Time":std_duration_hillClimbing, "Avg States Explored":statesHillClimbProm/30, "Std States Explored":stdStatesHill})
    results.append({"Tamaño Tablero": queens, "Algoritmo": "Simulated Annealing", "Porcentaje de Exito": str((solutionFondSimulatedAn/30)*100)+"%", "Avg Execution Time": AVG_duration_SimulatedAn/30 , "Std Execution Time":std_duration_SimulatedAn, "Avg States Explored":statesSimulatedAnProm/30, "Std Stes Explored":stdStatesSmAnn})
    results.append({"Tamaño Tablero": queens, "Algoritmo": "Genetic", "Porcentaje de Exito": str((solutionFondGenetic/30)*100)+"%", "Avg Execution Time": AVG_duration_genetic/30 , "Std Execution Time":std_duration_genetic, "Avg States Explored":statesGeneticProm/30, "Std States Explored": stdStatesGen})
    # print(results)
    print("Finished ",queens)
   


if __name__ == '__main__':
    start_time_General = time.time()
    results = []
    queens = [4,8,10,12,15]

    with multiprocessing.Pool(5) as pool:
        # Utiliza starmap para ejecutar la función con los argumentos
        pool.starmap(runner, [(queen, results) for queen in queens])
    
    print(time.time() - start_time_General)
    utils.save_to_csv(results)
