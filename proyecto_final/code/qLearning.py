import numpy as np
import enviorment4QL as enviorment
import csv

def get_next_action(state, q_values, epsilon):
    if np.random.random() > epsilon:
        action = np.argmax(q_values[state[0][0],state[1][0]])
        return action
    else:
        return np.random.randint(3)


env = enviorment.VizDoom(False)
observation_space = env.observation_space
print(observation_space.shape)
actions = [0,1,2] #Discrte(3) (left, right, shoot) [(1,0,0) (0,1,0) (0,0,1)]

q_values = np.zeros((observation_space.shape[0], observation_space.shape[1], 3))

discount_factor = 0.9 #factor de descuento para las recompensas futuras
# epsilon = 0.88 #porcentaje en que se tomara la mejor accion en vez de una aleatoria
learning_rate = 0.85 #tasa de aprendizaje

# epsilon_start = 0.88
epsilon_decay = 0.1
epsilon_end = 0.1
epsilon_decay_episodes = 20000


state,_ = env.reset()
print(state.shape)
episode_info = []
actions_list = []
six = 60000
q_values = np.load('C:/Users/arico/Documents/UNC/3ro/Inteligencias Artificial/ia-uncuyo-2023-develop/proyecto_final/q_values_episode_60000.npy')
episodes = 40000
for episode in range(episodes):
    state,_ = env.reset()
    # print(state.shape," ", np.reshape(state[0][0],120,1).shape," ", state[1].shape)
    actions_list = []
    done = False
    while not done:
        # state = env.game.get_state()
        # epsilon_decay = max(epsilon_start - (episode / epsilon_decay_episodes) * (epsilon_start - epsilon_end), epsilon_end)
        action = get_next_action(state, q_values, epsilon_decay)
        # print(action)
        actions_list.append(action)
        next_state, reward, done, _ , info = env.step(action)
        if done:
            episodee = episode + six
            with open('episode_info.txt', 'a') as txtfile:
                txtfile.write(f"Episode {episodee}, reward: {env.get_total_reward()}, length: {len(actions_list)}, epsilon: {epsilon_decay}\n")
            episode_info.append([episodee, env.get_total_reward(), len(actions_list)])
            next_state =np.squeeze(next_state)
            if episode % 20000 == 0:
                filename = f'q_values_episode_{episodee}.npy'
                np.save(filename, q_values)
        # print(len(np.reshape(state[0][0],120,1))," ", len(state[1])," ", len(next_np.reshape(state[0][0],120,1))," ", len(next_state[1]))

        q_values[state[0][0], state[1][0], action] += learning_rate * (reward + discount_factor * np.max(q_values[next_state[0][0], next_state[1][0],:]) - q_values[state[0][0], state[1][0], action])

        state = next_state

np.save('q_values.npy', q_values)

with open('episode_info.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write header
    csv_writer.writerow(['Episode', 'Reward', 'Num_Actions'])
    
    # Write episode information
    csv_writer.writerows(episode_info)