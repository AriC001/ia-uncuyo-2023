import csv
import math
import numpy as np
import matplotlib.pyplot as plt

def save_to_csv(results: list):
    with open("./tp5-busquedas-locales/busquedas-locales.csv", mode="a", newline="") as file:
        fieldnames = ["Tamaño Tablero", "Algoritmo", "Porcentaje de Exito", "Avg Execution Time", "Std Execution Time", "Avg States Explored", "Std States Explored" ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)

def standDev(data,prom):
    cont = 0
    for i in data:
        cont = cont + math.pow((i-prom),2)
    return math.sqrt((cont/29))

def plotTimes(hillC,SimAnn,Gen):
    plt.figure(figsize=(10, 6))
    plt.title("Distribución de los tiempos de ejecución (Boxplot 1)")
    plt.ylabel("Tiempo de ejecución")
    plt.boxplot([hillC, SimAnn, Gen], labels=['Hill Climbing', 'Simulated Annealing', 'Genetic'])
    plt.savefig("time1.png")  # Guarda el primer gráfico en un archivo
    plt.show()

    # Segundo boxplot
    plt.figure(figsize=(10, 6))
    plt.title("Distribución de los tiempos de ejecución (Boxplot 2)")
    plt.ylabel("Tiempo de ejecución")
    plt.boxplot([hillC, SimAnn], labels=['Hill Climbing', 'Simulated Annealing'])
    plt.savefig("time2.png")  # Guarda el segundo gráfico en un archivo
    plt.show()



    # plt.figure(figsize=(10, 6))
    # plt.title("Distribución de los tiempos de ejecución por Algoritmo")
    # # plt.xlabel("Algotimo")
    # plt.ylabel("Tiempo de ejecucion")
    # # usa boxplot para visualizar los datos
    # plt.boxplot([hillC,SimAnn,Gen],labels=['Hill Climbing', 'Simulated Annealing', 'Genetic'])
    # plt.savefig("time.png")  # guarda el gráfico en un archivo
    # plt.
    # plt.boxplot([hillC,SimAnn],labels=['Hill Climbing', 'Simulated Annealing'])
    # plt.savefig("time2.png")  # guarda el gráfico en un archivo
    # plt.show()

def plotFitness(data,Algth):
    plt.figure(figsize=(20, 12))
    plt.plot(data)
    plt.ylabel('Heurística')
    plt.xlabel('Estados')
    plt.title(f'Heurística por Estados explorados de {Algth} sin encontrar solución')
    plt.savefig(f"{Algth}_states_explored2.png")  # guarda el gráfico en un archivo
    # plt.show()

def plotFitness2(data,Algth):
    plt.figure(figsize=(20, 12))
    plt.plot(data)
    plt.ylabel('Heurística')
    plt.xlabel('Estados')
    plt.title(f'Heurística por Estados explorados de {Algth}')
    plt.savefig(f"{Algth}_states_explored2.png")  # guarda el gráfico en un archivo
    # plt.show()