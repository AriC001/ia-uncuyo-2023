import board as Board
import time
import csv

results = []
solutionFondHillClimb = 0
AVG_duration_hillClimbing = 0
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
    if tableros[0].value == 0:
        solutionFondHillClimb+=1
        print(solutionFondHillClimb,end=", ")
    # else:
    #     tableros[0].printear()
    #     print(tableros[0].value)
    #     print()
print()
porcentaje_str = str((solutionFondHillClimb/30)*100)
results.append({"Tamaño Tablero": 4, "Algoritmo": "Hill Climbing", "Porcentaje de Exito": porcentaje_str+"%", "Avg Execution Time": AVG_duration_hillClimbing/30 , "Std Execution Time":"", "Avg States Explored":"", "Std States Explored":"" })


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
    if tableros[0].value == 0:
        solutionFondHillClimb+=1
        print(solutionFondHillClimb,end=", ")
    # else:
    #     tableros[0].printear()
    #     print(tableros[0].value)
    #     print()

print()
porcentaje_str = str((solutionFondHillClimb/30)*100)
results.append({"Tamaño Tablero": 8, "Algoritmo": "Hill Climbing", "Porcentaje de Exito": porcentaje_str+"%", "Avg Execution Time": AVG_duration_hillClimbing/30 , "Std Execution Time":"", "Avg States Explored":"", "Std States Explored":"" })

tableros = sorted(tableros, key=lambda board: board.value, reverse=False)
tableros[0].printear()


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