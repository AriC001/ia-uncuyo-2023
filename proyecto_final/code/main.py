import random
import time
import os
import numpy as np
# Import the vizdoom for game environment
import vizdoom as vzd
# Import the OpenCV for image processing
import cv2

''' game configuration'''
# Create DoomGame instance. It will run the game and communicate with you.
game = vzd.DoomGame()
# Adds buttons that will be allowed to use.
game.load_config("./code/ViZDoom-master/scenarios/basic.cfg")

game.set_available_buttons(
    [vzd.Button.MOVE_LEFT, vzd.Button.MOVE_RIGHT, vzd.Button.ATTACK]
)
# Buttons that will be used can be also checked by:
print("Available buttons:", [b.name for b in game.get_available_buttons()])
# game.init()

game.set_screen_resolution(vzd.ScreenResolution.RES_640X480)

# Sets the screen buffer format. Not used here but now you can change it. Default is CRCGCB.
game.set_screen_format(vzd.ScreenFormat.RGB24)

# Enables buffer with a top-down map of the current episode/level (turned off by default).
game.set_automap_buffer_enabled(True)


# Adds game variables that will be included in state.  #Optional because is config by default
game.set_available_game_variables([vzd.GameVariable.AMMO2])
print(
    "Available game variables:",
    [v.name for v in game.get_available_game_variables()],
)

# Causes episodes to finish after 200 tics (actions)
game.set_episode_timeout(200) #instead of 300 (default)

# Makes episodes start after 10 tics (~after raising the weapon)
game.set_episode_start_time(10)

# Makes the window appear (turned on by default)
game.set_window_visible(True)

# Sets the living reward (for each move) to -1
game.set_living_reward(-1)

#in order to visualize depth buffer, you need to enable it first
game.set_depth_buffer_enabled(True)

# Initialize the game. Further configuration won't take any effect from now on.
game.init()

'''end of game configuration'''
#actions = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
#actions[0]= Move Left | actions[1]= Move Right | actions[2]= Attack 
actions = np.identity(3, dtype=int) # [[1,0,0],[0,1,0],[0,0,1]]
game.new_episode() #Starts a new episode


'''experimental screen buffers tests'''   
# state = game.get_state() #get the state of the game with the screen buffer and game variables
# img = state.screen_buffer #get the screen buffer, the image that is rendered of the game frame by frame in an array of pixels in RGB24 format
# print(img)
# print(img.shape) # set by set_screen_resolution(vzd.ScreenResolution.RES_640X480)

# # Depth buffer, always in 8-bit gray channel format.
# depth = state.depth_buffer
# print(depth)
# cv2.imshow("ViZDoom Depth Buffer", depth)
# cv2.waitKey(0) # Press Enter to continue
# exit()
''' end of experimental screen buffers tests'''

'''random movement agent test'''
episodes = 5

for episode in range(episodes):
    game.new_episode() #Starts a new episode
    while not game.is_episode_finished(): #check if episode is not finished
        state = game.get_state() #get the state of the game with the screen buffer and game variables
        img = state.screen_buffer #get the screen buffer, the image that is rendered of the game frame by frame in an array of pixels in RGB24 format
        ammo = state.game_variables
        action = random.choice(actions) #randomly choose an action from the set of posible actions
        reward = game.make_action(action) #make an action and get the reward
        print("\treward:", reward, end=" ")
        time.sleep(0.02)
    print("Result:", game.get_total_reward()) #print the total reward
    time.sleep(2)
'''end of random movement agent test'''