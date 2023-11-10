from environment import Environment
from aStar import *
import utils

results = [] 
statesExplored = []    
for i in range(30):
    # Create an environment 
    env = Environment(100)

    # # Run the A* algorithm
    # solution = aStar.aStar(ag)


    optimal_path = aStar(env, (env.start[0],env.start[1]), (env.finish[0],env.finish[1]))
    if optimal_path:
        # print(optimal_path)
        results.append(len(optimal_path) - 1)
        statesExplored.append(env.statesExplored)  
    
# # Plot the solution
print(results.__len__())
utils.plotFitness(statesExplored,"A*")
print(utils.prom(statesExplored))
print(utils.standDev(statesExplored,utils.prom(statesExplored)))