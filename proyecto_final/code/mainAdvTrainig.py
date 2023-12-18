import random
import os
import numpy as np
# import enviorment4
import enviorment
import cv2
from stable_baselines3.common.env_checker import check_env
import vizdoom as vzd
import time
import utils

'''experimental screen buffers tests'''   
# state = game.get_state() #get the state of the game with the screen buffer and game variables
# img = state.screen_buffer #get the screen buffer, the image that is rendered of the game frame by frame in an array of pixels in RGB24 format
# print(img)
# print(img.shape) # set by set_screen_resolution(vzd.ScreenResolution.RES_640X480)

# # # Depth buffer, always in 8-bit gray channel format.
# depth = state.depth_buffer
# cv2.resize(depth, (160, 120)) # resize in case that resolution is too big to procces quickly
# print(depth)
# cv2.imshow("ViZDoom Depth Buffer", depth)
# print(depth.shape)
# cv2.waitKey(0) # Press Enter to continue
# exit()
''' end of experimental screen buffers tests'''





from stable_baselines3 import PPO, A2C
from stable_baselines3.common.callbacks import CheckpointCallback

'''Train'''


env = enviorment.VizDoom(False,env_selection="defend_the_line")
# Save a checkpoint every 1000 steps
checkpoint_callback = CheckpointCallback(
  save_freq=10000,
  # save_path="./proyecto_final/logs/TurningPPO",
  save_path="./logs",
  # name_prefix="PPO_model",
  name_prefix="A2C_model",
  save_replay_buffer=True,
  save_vecnormalize=True,
)

# # modelElTr = A2C("CnnPolicy", env, verbose=1,learning_rate=0.003, batch_size=128, gae_lambda=0)
# # model2 = A2C("CnnPolicy", env,tensorboard_log="./proyecto_final/tensorLogs" , verbose=1,learning_rate=0.003)
model = PPO("CnnPolicy", env,tensorboard_log="./proyecto_final/tensorLogs",verbose=1,learning_rate=0.00027, batch_size=64)
model.learn(total_timesteps = 100000, callback=checkpoint_callback)

# remove to demonstrate saving and loading
# env.close()
# del env
# model.set_env(env)
# model.learn(total_timesteps = 100000, callback=checkpoint_callback2)
# env.close()
# del env
'''End Train'''


'''Test'''
# env = enviorment.VizDoom(True,env_selection="defend_the_line")
# env = enviorment.VizDoom(False,env_selection="defend_the_line")
# PPO.set_env(model,env)
# model.learn(total_timesteps = 150000, callback=checkpoint_callback)
# env.close()
# del env
# del model


env = enviorment.VizDoom(True,env_selection="defend_the_center")
# model = PPO.load("./proyecto_final/logs/TurningPPO/PPO_model_150000_steps")
model = PPO.load("./proyecto_final/logs/WorkingPPO/PPO_model_100000_steps")
#env = enviorment.VizDoom(True,env_selection = "defend_the_center")
#model = PPO.load("./proyecto_final/logs/TurningPPO/PPO_model_150000_steps")

cont = 0
episode_info = []
actions_list = []
actionsProm = 0
actionsTotal = 0
rewardProm = 0
obs, _ = env.reset()
while True:
  action, _states = model.predict(obs)
  actionsTotal+=1
  # print(_states)
  # print(action)
  obs, reward, done, _ ,info = env.step(action)
  # print(obs.shape, " ", obs[0].shape, " ", obs[1].shape)
  # time.sleep(0.028)
  if done:
    print("Episode finished, reward:", env.get_total_reward())
    rewardProm += env.get_total_reward()
    episode_info.append(env.get_total_reward())
    actionsProm +=actionsTotal
    actions_list.append(actionsTotal)
    actionsTotal = 0
    obs,_ = env.reset()
    cont +=1
    if cont == 1:
      env.game.close()
      break
    
print("Promedio rewards ",rewardProm/30)
print("Desviacion estandar rewards ",utils.standDev(episode_info,rewardProm/30))
print("Promedio duracion episodio ",actionsProm/30)
print("Desviacion estandar duracion episodio ",utils.standDev(actions_list,actionsProm/30))
    
'''End Test'''


'''random movement agent test'''
# episodes = 5

# for episode in range(episodes):
#     game.new_episode() #Starts a new episode
#     while not game.is_episode_finished(): #check if episode is not finished
#         state = game.get_state() #get the state of the game with the screen buffer and game variables
#         img = state.screen_buffer #get the screen buffer, the image that is rendered of the game frame by frame in an array of pixels in RGB24 format
#         ammo = state.game_variables
#         action = random.choice(actions) #randomly choose an action from the set of posible actions
#         reward = game.make_action(action) #make an action and get the reward
#         print("\treward:", reward, end=" ")
#         time.sleep(0.02)
#     print("Result:", game.get_total_reward()) #print the total reward
#     time.sleep(2)
'''end of random movement agent test'''




'''Gym implemetation '''


# class CustomEnv(gym.Env):
   

