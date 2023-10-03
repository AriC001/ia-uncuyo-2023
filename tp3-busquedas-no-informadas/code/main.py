from enviorment import Environment
from agent import Agent
from node import *


env = Environment()
nodificar(env)

costsBFS = []
costsDFS = []
for i in range(30):
    env = Environment()
    nodificar(env)
    agent1 = Agent(env)
    agent2 = Agent(env)
    # road = env.generateRoad(agent.BFS())
    ##   BFS
    road = agent1.BFS()
    env.visit()
    costsBFS.append(agent1.cost)

    ##DFS
    agent2.generateRoadDFS(agent2.start)
    env.visit()
    costsDFS.append(agent2.cost)
print(min(costsDFS))
print(costsDFS)
print(min(costsBFS))
print(costsBFS)

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




    