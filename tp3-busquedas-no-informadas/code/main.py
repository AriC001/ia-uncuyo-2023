from enviorment import Environment
from agent import Agent
from node import *


env = Environment()
nodificar(env)

costsBFS = []
costsDFS = []
costsDFSLimit = []
resultBFS = []
resultDFS = []
resultDFS_L = []
results=[]
for i in range(30):
    env = Environment()
    nodificar(env)
    agent1 = Agent(env,"BFS")
    agent2 = Agent(env,"DFS")
    agent3 = Agent(env,"DFS-L")
    # road = env.generateRoad(agent.BFS())
    ##   BFS
    road = agent1.BFS()
    env.visit()
    costsBFS.append(agent1.state)

    ##DFS
    agent2.generateRoadDFS(agent2.start)
    env.visit()
    costsDFS.append(agent2.state)

    #Limit DFS
    agent3.limitDFS(agent3.start,agent1.state)
    env.visit()
    costsDFSLimit.append(agent3.state)

    results.append({"Agent": agent1.name,"iteration": i, "states_explored": agent1.state,
            "solution_found": agent1.solutionFound, "path_cost": agent1.cost})
    results.append({"Agent": agent2.name,"iteration": i, "states_explored": agent2.state,
            "solution_found": agent2.solutionFound, "path_cost": agent2.cost})
    results.append({"Agent": agent3.name,"iteration": i, "states_explored": agent3.state,
            "solution_found": agent3.solutionFound, "path_cost": agent3.cost})
# print(min(costsDFS))
print(costsDFS)
# print(min(costsBFS))
print(costsBFS)
print(costsDFSLimit)

costsBFS2 = []
for data in costsBFS:
    if data is not None:
        costsBFS2.append(data)
        

costsDFS2 = []
for data in costsDFS:
    if data is not None:
        costsDFS2.append(data)

costsDFSL2 = []
for data in costsDFSLimit:
    if data is not None:
        costsDFSL2.append(data)

import numpy as np
import matplotlib.pyplot as plt
import csv


def save_to_csv(results: list):
    with open("no-informada-results.csv", mode="w", newline="") as file:
        fieldnames = ["Agent", "states_explored", "solution_found", "path_cost"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)

save_to_csv(results)

plt.figure(figsize=(10, 6))
plt.title("Estados Explorados por Agente")
plt.xlabel("Agente")
plt.ylabel("Estados Explorados")
# usa boxplot para visualizar los datos
plt.boxplot([costsBFS2,costsDFS2,costsDFSL2],labels=['BFS', 'DFS', 'DFS-Limit'])
# plt.savefig("states_explored.png")  # guarda el gráfico en un archivo
plt.show()

print()

##   DFS
# for i in range(30):
#     # env = Environment()
#     # nodificar(env)
#     agent = Agent(env)
#     road = agent.generateRoadDFS(agent.start)
#     # print(road)
#     env.visit()
#     costsDFS.append(agent.cost)
# print(min(costsDFS))
# print(costsDFS)




    