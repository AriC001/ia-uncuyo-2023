import csv
import math
import numpy as np
import matplotlib.pyplot as plt

def save_to_csv(results: list):
    with open("./tp6-csp/csp.csv", mode="a", newline="") as file:
        fieldnames = ["Tamaño", "Algortimo","Sol Found" ,"AVG Time", "STD Time","AVG States","STD States"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # writer.writeheader()
        writer.writerows(results)

def standDev(data,prom):
    cont = 0
    for i in data:
        cont = cont + math.pow((i-prom),2)
    return math.sqrt((cont/29))

# def plotTimes(Back,Forw,queens):
#     plt.figure(figsize=(10, 6))
#     plt.title("Distribución de los tiempos de ejecución")
#     plt.ylabel("Tiempo de ejecución")
#     plt.boxplot([Back,Forw], labels=['Backtracking','Forward Checking'])
#     plt.savefig(f"./tp6-csp/pics/time {queens}.png")  # Guarda el segundo gráfico en un archivo
#     plt.show()



# import matplotlib.pyplot as plt

# # Datos de tiempos de ejecución para Backtracking y Forward Checking
# tamanos = [4, 8, 10, 12]
# tiempos_backtracking = [0.0001668, 0.0674277, 1.4737879, 43.6867254]
# tiempos_forward_checking = [0.0005338, 0.0021687, 0.0060386, 0.0108429]

# # Datos de cantidad de estados recorridos para Backtracking y Forward Checking
# estados_backtracking = [62.0, 124.0, 155.0, 186.0]
# estados_forward_checking = [62.0, 230.9333, 365.0, 482.0]

# # Crear gráfico de caja para tiempos de ejecución (Backtracking)
# plt.figure(figsize=(10, 6))
# plt.title("Comparación de Tiempos de Ejecución para Backtracking")
# plt.xlabel("Tamaño del problema (Reinas)")
# plt.ylabel("Tiempo de ejecución")
# plt.bar(tamanos, tiempos_backtracking, tick_label=tamanos)
# plt.savefig("./tp6-csp/pics/Back_Times.png")
# plt.show()

# # Crear gráfico de caja para tiempos de ejecución (Forward Checking)
# plt.figure(figsize=(10, 6))
# plt.title("Comparación de Tiempos de Ejecución para Forward Checking")
# plt.xlabel("Tamaño del problema (Reinas)")
# plt.ylabel("Tiempo de ejecución")
# plt.bar(tamanos, tiempos_forward_checking, tick_label=tamanos)
# plt.savefig("./tp6-csp/pics/Forw_Times.png")
# plt.show()

# # Crear gráfico de caja para cantidad de estados recorridos (Backtracking)
# plt.figure(figsize=(10, 6))
# plt.title("Comparación de Cantidad de Estados Recorridos para Backtracking")
# plt.xlabel("Tamaño del problema (Reinas)")
# plt.ylabel("Estados Recorridos")
# plt.bar(tamanos, estados_backtracking, tick_label=tamanos)
# plt.savefig("./tp6-csp/pics/Back_States.png")
# plt.show()

# # Crear gráfico de caja para cantidad de estados recorridos (Forward Checking)
# plt.figure(figsize=(10, 6))
# plt.title("Comparación de Cantidad de Estados Recorridos para Forward Checking")
# plt.xlabel("Tamaño del problema (Reinas)")
# plt.ylabel("Estados Recorridos")
# plt.bar(tamanos, estados_forward_checking, tick_label=tamanos)
# plt.savefig("./tp6-csp/pics/Forw_States.png")
# plt.show()
