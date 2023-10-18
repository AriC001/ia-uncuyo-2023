import board as Board
import time
import csv
from random import sample
import math

# tableros = []
# tableros2 = []
# queens = 12
# for i in range(queens):
#     board = Board.Board(queens)
#     board2 = Board.Board(queens)
#     tableros.append(board)
#     tableros2.append(board2)
# cont = 0
# # while tableros[0].value > 0 and cont < 1:
# start1 = time.time()
# for i in range(0,12):
#     tableros[i].simulatedAnnealing2()
# print(time.time()-start1)
# tableros = sorted(tableros, key=lambda board: board.value, reverse=False)

# start1 = time.time()
# for i in range(0,12):
#     tableros2[i].simulatedAnnealing()
# print(time.time()-start1)
# tableros2 = sorted(tableros2, key=lambda board: board.value, reverse=False)

# for i in range(0,4):
#     tableros[i].printear()
#     print(tableros[i].value)
#     print()
# print("----------")
# for i in range(0,4):
#     tableros2[i].printear()
#     print(tableros2[i].value)
#     print()



# temperature = 1000
# cool = 0.92
# cont=0
# for i in range(200):
#     if (math.exp((2 - 3) / temperature)) >0.09:
#         cont+=1
#     temperature*=cool
# print(cont)
# exit()

results = []
solutionFondHillClimb = 0
AVG_duration_hillClimbing = 0
solutionFondSimulatedAn = 0
AVG_duration_SimulatedAn = 0
for i in range(30): # Creacion de 4 tableros con 4 reinas
    tableros = []
    queens = 4
    for i in range(queens):
        board = Board.Board(queens)
        tableros.append(board)

    tableros = sorted(tableros, key=lambda board: board.value, reverse=False)
    start_time_hillClimbing = time.time()

    cont = 0
    while tableros[0].value > 0 and cont < 100:
        for i in range(0,tableros.__len__()):
            tableros[i].hillClimbing()
        tableros = sorted(tableros, key=lambda board: board.value, reverse=False)
        cont+=1
    duration_hillClimbing = time.time() - start_time_hillClimbing
    AVG_duration_hillClimbing += duration_hillClimbing
    tableros = sorted(tableros, key=lambda board: board.value, reverse=False)
    # print("Hill: ",end="")
    for i in range(0,tableros.__len__()):
        if tableros[i].value == 0:
            solutionFondHillClimb+=1
        # print(solutionFondHillClimb,end=", ")
    # print()
    tableros = []
    queens = 4
    for i in range(queens):
        board = Board.Board(queens)
        tableros.append(board)
    start_time_SimulatedAn = time.time()
    for i in range(0,tableros.__len__()):
        tableros[i].simulatedAnnealing()
    tableros = sorted(tableros, key=lambda board: board.value, reverse=False)
    duration_SimulatedAn = time.time() - start_time_SimulatedAn

    # print("Anne: ",end="")
    # AVG_duration_SimulatedAn += duration_SimulatedAn
    for i in range(0,tableros.__len__()):
        if tableros[i].value == 0:
            solutionFondSimulatedAn+=1
        # print(solutionFondSimulatedAn,end=", ")
    # print()
    # else:
    #     tableros[0].printear()
    #     print(tableros[0].value)
    #     print()
# print()
# porcentaje_str = str((solutionFondHillClimb/30)*100)
results.append({"Tamaño Tablero": 4, "Algoritmo": "Hill Climbing", "Porcentaje de Exito": str((solutionFondHillClimb/30)*100)+"%", "Avg Execution Time": AVG_duration_hillClimbing/30 , "Std Execution Time":"", "Avg States Explored":"", "Std States Explored":"" })
results.append({"Tamaño Tablero": 4, "Algoritmo": "Simulated Annealing", "Porcentaje de Exito": str((solutionFondSimulatedAn/30)*100)+"%", "Avg Execution Time": AVG_duration_SimulatedAn/30 , "Std Execution Time":"", "Avg States Explored":"", "Std States Explored":"" })


solutionFondHillClimb = 0
AVG_duration_hillClimbing = 0
for i in range(30): # Creacion de 8 tableros con 8 reinas
    tableros = []
    queens = 8
    for i in range(queens):
        board = Board.Board(queens)
        tableros.append(board)

    tableros = sorted(tableros, key=lambda board: board.value, reverse=False)
    start_time_hillClimbing = time.time()

    cont = 0
    while tableros[0].value > 0 and cont < 100:
        for i in range(0,tableros.__len__()):
            tableros[i].hillClimbing()
        tableros = sorted(tableros, key=lambda board: board.value, reverse=False)
        cont+=1
    duration_hillClimbing = time.time() - start_time_hillClimbing
    AVG_duration_hillClimbing += duration_hillClimbing
    tableros = sorted(tableros, key=lambda board: board.value, reverse=False)

    # print("Hill: ",end="")
    if tableros[0].value == 0:
        solutionFondHillClimb+=1
        # print(solutionFondHillClimb,end=", ")
    # else:
    #     tableros[0].printear()
    #     print(tableros[0].value)
    #     print()

# print()
porcentaje_str = str((solutionFondHillClimb/30)*100)
results.append({"Tamaño Tablero": 8, "Algoritmo": "Hill Climbing", "Porcentaje de Exito": porcentaje_str+"%", "Avg Execution Time": AVG_duration_hillClimbing/30 , "Std Execution Time":"", "Avg States Explored":"", "Std States Explored":"" })

# tableros = sorted(tableros, key=lambda board: board.value, reverse=False)
# tableros[0].printear()


# for i in range(0,tableros.__sizeof__(),2):
#     tableros[i].crossJoin(tableros[i+1])


# for i in range(queens):
#     tableros[i].printear()
#     print(tableros[i].value)
#     print()


def save_to_csv(results: list):
    with open("./tp5-busquedas-locales/busquedas-locales.csv", mode="a", newline="") as file:
        fieldnames = ["Tamaño Tablero", "Algoritmo", "Porcentaje de Exito", "Avg Execution Time", "Std Execution Time", "Avg States Explored", "Std States Explored" ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)

save_to_csv(results)