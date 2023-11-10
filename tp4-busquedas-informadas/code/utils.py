import csv
import math
import numpy as np
import matplotlib.pyplot as plt

def save_to_csv(results: list):
    with open("./tp5-busquedas-locales/busquedas-locales.csv", mode="a", newline="") as file:
        fieldnames = [""]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)

def standDev(data,prom):
    cont = 0
    for i in data:
        cont = cont + math.pow((i-prom),2)
    return math.sqrt((cont/29))

def prom(data):
    cont = 0
    for i in data:
        cont = cont + i
    return cont/data.__len__()


def plotFitness(data,Algth):
    plt.figure(figsize=(10, 6))
    plt.boxplot(data)
    plt.ylabel('Estados explorados')
    plt.xlabel('')
    plt.title(f'Distribución de estados explorados para encontrar el caminos óptimos para {Algth}')
    plt.savefig("./tp4-busquedas-informadas/pics/AStar_states_explored.png")  # guarda el gráfico en un archivo
    # plt.show()

def plotFitness2(data,Algth):
    plt.figure(figsize=(20, 12))
    plt.plot(data)
    plt.ylabel('Heurística')
    plt.xlabel('Estados')
    plt.title(f'Heurística por Estados explorados de {Algth}')
    plt.savefig(f"AStar_states_explored2.png")  # guarda el gráfico en un archivo
    # plt.show()