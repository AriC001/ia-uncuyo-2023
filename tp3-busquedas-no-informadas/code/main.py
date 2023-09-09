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







    