from enviorment0 import Environment
from agent0 import Agent

StatSaverRacional= []
StatSaverRandom = []

#2x2, 4x4, 8x8, 16x16, 32x32, 64x64, 128x128
sizes=[2,4,8,16,32,64,128]
dirtRate=[0.1,0.2,0.4,0.8]

#Racional
w=0
for k in range(len(dirtRate)):
    for j in range(len(sizes)):
        for i in range(10):
            env= Environment(dirtRate[k],sizes[j])
            agent1 = Agent(env)
            while(agent1.remaining_moves > 0 and env.dirty_squares > 0):
                agent1.perspective()
            StatSaverRacional.append("Estadistica [" + str(i) + "] para DirtRate [" + str(dirtRate[k]) + "] para size [" + str(sizes[j]) + "] Resultados: Puntos:[" + str(agent1.points) + "] Total de dirt [" + str(env.total_dirt_squares) + "] restante: [" + str(env.dirty_squares) +"] Movimientos Res [" + str(agent1.remaining_moves) +"]" + '\n')
            w+=1
            agent1.reset()
k=0
j=0
i=0
for k in range(len(dirtRate)):
    for j in range(len(sizes)):
        for i in range(10):
            env1= Environment(dirtRate[k],sizes[j])
            agentRandom = Agent(env1)
            while(agentRandom.remaining_moves > 0 and env1.dirty_squares > 0):
                agentRandom.think()
            StatSaverRandom.append("Estadistica [" + str(i) + "] para DirtRate [" + str(dirtRate[k]) + "] para size [" + str(sizes[j]) + "] Resultados: Puntos:[" + str(agentRandom.points) + "] Total de dirt [" + str(env1.total_dirt_squares) + "] restante: [" + str(env1.dirty_squares) +"] Movimientos Res [" + str(agentRandom.remaining_moves) +"]" + '\n')
            w+=1
            agentRandom.reset()

print(w)
file = open("Stats dump Racional.txt",'a')
file.writelines(StatSaverRacional)
file.close()
file = open("Stats dump Random.txt",'a')
file.writelines(StatSaverRandom)
file.close()
#print(StatSaverRacional)





