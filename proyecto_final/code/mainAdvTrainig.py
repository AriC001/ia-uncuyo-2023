import random
import os
import numpy as np
# import enviorment4
import enviorment
import cv2
from stable_baselines3.common.env_checker import check_env
import vizdoom as vzd
import time
''' game configuration'''
# # Create DoomGame instance. It will run the game and communicate with you.
# game = vzd.DoomGame()
# # Adds buttons that will be allowed to use.
# game.load_config("./basic.cfg")

# game.set_available_buttons(
#     [vzd.Button.MOVE_LEFT, vzd.Button.MOVE_RIGHT, vzd.Button.ATTACK]
# )
# # Buttons that will be used can be also checked by:
# print("Available buttons:", [b.name for b in game.get_available_buttons()])
# # game.init()

# game.set_screen_resolution(vzd.ScreenResolution.RES_640X480)

# # Sets the screen buffer format. Not used here but now you can change it. Default is CRCGCB.
# game.set_screen_format(vzd.ScreenFormat.RGB24)

# # Enables buffer with a top-down map of the current episode/level (turned off by default).
# game.set_automap_buffer_enabled(True)


# # Adds game variables that will be included in state.  #Optional because is config by default
# game.set_available_game_variables([vzd.GameVariable.AMMO2])
# print(
#     "Available game variables:",
#     [v.name for v in game.get_available_game_variables()],
# )

# # Causes episodes to finish after 200 tics (actions)
# game.set_episode_timeout(200) #instead of 300 (default)

# # Makes episodes start after 10 tics (~after raising the weapon)
# game.set_episode_start_time(10)

# # Makes the window appear (turned on by default)
# game.set_window_visible(True)

# # Sets the living reward (for each move) to -1
# game.set_living_reward(-1)

# #in order to visualize depth buffer, you need to enable it first
# game.set_depth_buffer_enabled(True)

# # Initialize the game. Further configuration won't take any effect from now on.
# game.init()

'''end of game configuration'''


# game.new_episode() #Starts a new episode



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




# It will check your custom environment and output additional warnings if needed
# exit()
from stable_baselines3 import PPO, A2C
from stable_baselines3.common.callbacks import CheckpointCallback
# grayscaledImg, reward, done, truncated,ammo = env.step(random.choice([0,1,2]))
# env = enviorment.VizDoom()
# print(check_env(env))


env = enviorment.VizDoom(False,env_selection="defend_the_line")
# Save a checkpoint every 1000 steps
checkpoint_callback = CheckpointCallback(
  save_freq=25000,
  # save_path="./proyecto_final/logs/TurningPPO",
  save_path="./proyecto_final/logs",
  # name_prefix="PPO_model",
  name_prefix="A2C_model",
  save_replay_buffer=True,
  save_vecnormalize=True,
)

# # modelElTr = A2C("CnnPolicy", env, verbose=1,learning_rate=0.003, batch_size=128, gae_lambda=0)
# # model2 = A2C("CnnPolicy", env,tensorboard_log="./proyecto_final/tensorLogs" , verbose=1,learning_rate=0.003)
# model = PPO("CnnPolicy", env,tensorboard_log="./proyecto_final/tensorLogs",verbose=1,learning_rate=0.00027, batch_size=64)
# model.learn(total_timesteps = 100000, callback=checkpoint_callback)

# remove to demonstrate saving and loading
# env.close()
# del env
# env = enviorment4.VizDoom(True)
# model.set_env(env)
# model.learn(total_timesteps = 100000, callback=checkpoint_callback2)
# env.close()
# del env
# env = enviorment.VizDoom(True,env_selection="defend_the_line")


# env = enviorment.VizDoom(False,env_selection="defend_the_line")
# model = PPO.load("./proyecto_final/logs/PPO_model_90000_steps")
# PPO.set_env(model,env)
# model.learn(total_timesteps = 150000, callback=checkpoint_callback)
# env.close()
# del env
# del model


env = enviorment.VizDoom(True,env_selection="defend_the_center")
model = PPO.load("./proyecto_final/logs/TurningPPO/PPO_model_150000_steps")
# model = PPO.load("./proyecto_final/logs/WorkingPPO/PPO_model_100000_steps")
cont = 0
# # # env.game.new_episode(f"./proyecto_final/replays/episode{cont}_rec.lmp")
obs, _ = env.reset()
while True:
  action, _states = model.predict(obs)
  # print(_states)
  # print(action)
  obs, reward, done, _ ,info = env.step(action)
  # print("act: ",action," rew: ",env.get_total_reward())
  time.sleep(0.028)
  if done:
    print("Episode finished, reward:", env.get_total_reward())
    obs,_ = env.reset()
    cont +=1
    if cont == 1:
      env.game.close()
      break
    
# print("shapee ",grayscaledImg.shape)  
# print(env.observation_space)
# cv2.imshow("ViZDoom Depth Buffer", grayscaledImg)
# cv2.waitKey(0)
# while not done:
#     grayscaledImg, reward, done, ammo = env.step(random.choice([0,1,2]))
#     print(env.action_space)

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
   

