from enviorment import Environment
from agent import Agent
from node import *


env = Environment()
nodificar(env)

##   BFS
costsBFS = []
for i in range(30):
    agent = Agent(env)
    road = env.generateRoad(agent.BFS())
    env.visit()
    costsBFS.append(agent.cost)
print(min(costsBFS))

##   DFS
costsDFS = []
for i in range(30):
    agent = Agent(env)
    road = agent.generateRoadDFS(agent.start)
    # print(road)
    env.visit()
    costsDFS.append(agent.cost)
print(min(costsDFS))




    