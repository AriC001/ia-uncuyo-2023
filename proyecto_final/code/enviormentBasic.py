import gymnasium as gym
from gymnasium import spaces
# Import the OpenCV for image processing
import cv2
import numpy as np
import vizdoom as vzd
import time
from typing import Optional
import random

class VizDoom(gym.Env):
    """Custom Environment that follows gym interface."""

    # metadata = {"render_modes": ["human"], "render_fps": 30}

    def __init__(self, render = False):
        super().__init__()
        ''' '''
        ''' '''
        self.game = vzd.DoomGame()

        self.game.load_config("./basic.cfg")

        # Adds buttons that will be allowed to use.
        self.game.set_available_buttons(
            [vzd.Button.MOVE_LEFT, vzd.Button.MOVE_RIGHT, vzd.Button.ATTACK]
        )

        # Buttons that will be used can be also checked by:
        print("Available buttons:", [b.name for b in self.game.get_available_buttons()])

        self.game.set_screen_resolution(vzd.ScreenResolution.RES_640X480)

        # Sets the screen buffer format. Not used here but now you can change it. Default is CRCGCB.
        self.game.set_screen_format(vzd.ScreenFormat.RGB24)
        
        # Enables buffer with a top-down map of the current episode/level (turned off by default).
        self.game.set_automap_buffer_enabled(True)

        # Adds game variables that will be included in state.  #Optional because is config by default
        self.game.set_available_game_variables([vzd.GameVariable.AMMO2])
        print(
            "Available game variables:",
            [v.name for v in self.game.get_available_game_variables()],
        )

        # Causes episodes to finish after 200 tics (actions)
        self.game.set_episode_timeout(200) #instead of 300 (default)

        # Makes episodes start after 10 tics (~after raising the weapon)
        # self.game.set_episode_start_time(10)

        # Makes the window appear (turned on by default)
        if render == False:
            self.game.set_window_visible(False)
        else:
            self.game.set_window_visible(True)

        # Sets the living reward (for each move) to -1
        self.game.set_living_reward(-1.2)
        
        # Sets the shooting reward (for each shoot) to -10
        # self.game.set_shotgun_reward(-10)

        # Enables labeling of in-game objects labeling (turned off by default).
        # self.game.set_labels_buffer_enabled(True)
        # Enables information about all objects present in the current episode/level.
        self.game.set_objects_info_enabled(True)

        # Enables information about all sectors (map layout).
        # self.game.set_sectors_info_enabled(True)

        self.game.add_available_game_variable(vzd.GameVariable.POSITION_X)
        self.game.add_available_game_variable(vzd.GameVariable.POSITION_Y)

        # In order to visualize depth buffer, you need to enable it first
        # self.game.set_depth_buffer_enabled(True)

        # Initialize the game. Further configuration won't take any effect from now on.
        self.game.init()
        

        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(3)
        ''' '''
        ''' '''
        # Example for using image as input (channel-first; channel-last also works):
        self.observation_space = spaces.Box(low=0, high=255, shape=(120,160,1), dtype=np.uint8)

    def grayScale(self):
        """This solution does not work because the depth buffer is not in 8-bit gray channel format"""
        # grayScaledImg = self.game.get_state().depth_buffer
        # # shape = observation.shape
        # grayScaledImg = cv2.resize(grayScaledImg, (160,120), interpolation = cv2.INTER_CUBIC)
        # grayScaledImg = np.reshape(grayScaledImg, (grayScaledImg.shape[0], grayScaledImg.shape[1], 1))
        # grayScaledImg = np.stack((grayScaledImg,)*3, axis=-1)
        # print(grayScaledImg)
        # print(grayScaledImg.shape)
        # cv2.waitKey(0) 

        """crop and grayscaled screen buffer instead of depth buffer"""
        screenBuffer = self.game.get_state().screen_buffer
        # print(screenBuffer.shape)
        screenBuffer = cv2.cvtColor(screenBuffer,cv2.COLOR_BGR2GRAY)
        # cv2.imshow("oroginal", screenBuffer)
        cropScreenBuffer = screenBuffer[0:405, 0:640]
        cropScreenBuffer = cv2.resize(cropScreenBuffer, (160,120), interpolation = cv2.INTER_CUBIC)
        cropScreenBuffer = np.reshape(cropScreenBuffer, (120, 160,1))
        # print(cropScreenBuffer.shape)
        # print(self.observation_space.shape)
        # print(cropScreenBuffer)
        # cv2.imshow("cropped", cropScreenBuffer)
        # cv2.waitKey(0)

        return cropScreenBuffer

    def step(self, action):
        #actions = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        #actions[0]= Move Left | actions[1]= Move Right | actions[2]= Attack 
        actions = np.identity(3, dtype=np.uint8) # [[1,0,0],[0,1,0],[0,0,1]]
        # action = random.choice(actions) #randomly choose an action from the set of posible actions
        frameSkip = 1 #number of frames to skip
        reward = self.game.make_action(actions[action],2) #make an action and get the reward
        # reward = self.game.make_action(action)
        if self.game.get_state():
            state = self.game.get_state() #get the state of the game with the screen buffer and game variables
            img = state.screen_buffer #get the screen buffer, the image that is rendered of the game frame by frame in an array of pixels in RGB24 format
            grayScaledImg = self.grayScale()
            # grayscaledImg = state.depth_buffer #get the depth buffer, the image that is rendered of the game frame by frame in an array of pixels in 8-bit gray channel format
            # grayscaledImg = np.repeat(state.depth_buffer[...], repeats=2, axis=1)
            # shape=(48,64,3)
            # grayscaledImg = cv2.resize(grayscaledImg, shape[::-1])
            # grayscaledImg = np.stack([grayscaledImg] * 3, axis=2)
            """  get enemy and player position """
            # enemy = state.objects[0] if state.objects[0].name == "Cacodemon" else state.objects[1]
            # player = state.objects[0] if state.objects[0].name == "DoomPlayer" else state.objects[1]
            # print(enemy.name)
            # print("X: ",enemy.position_x,", Y: ",enemy.position_y)
            # print(player.name)
            # print("X: ",player.position_x,", Y: ",player.position_y)
            # time.sleep(4)
            """  """
            # print()
            info = {"ammo": 0}
            info["ammo"] = state.game_variables[0]
        else:
            grayScaledImg = np.zeros(self.observation_space.shape,dtype=np.uint8)
            info = {"ammo": 0}
            # info["ammo"] = state.game_variables[0]
        truncated = False  # Truncation to be handled by the TimeLimit wrapper
        # print("\treward:", reward, end=" ")
        return grayScaledImg, reward, self.game.is_episode_finished(), truncated,info

    def reset(
        self,
        *,
        seed: Optional[int] = None,
        options: Optional[dict] = None,
    ):
        super().reset(seed=seed)
        # if seed is not None:
        #     self.game.set_seed(seed)
        self.game.new_episode()
        # self.game.new_episode()
        state = self.game.get_state()
        enemy = state.objects[0] if state.objects[0].name == "Cacodemon" else state.objects[1]
        player = state.objects[0] if state.objects[0].name == "DoomPlayer" else state.objects[1]
        positions = (abs(enemy.position_y) - abs(player.position_y))
        # print("resta: ", positions)
        # print(enemy.name)
        # print("X: ",enemy.position_x,", Y: ",enemy.position_y)
        # print(player.name)
        # print("X: ",player.position_x,", Y: ",player.position_y)
        while positions > (-35) and positions < 50: #if the enemy is too close to the player
            # print("resta: ", positions)
            # print(enemy.name)
            # print("X: ",enemy.position_x,", Y: ",enemy.position_y)
            if enemy.position_y > 0 and random.random() < 0.8:
                self.game.new_episode()
            # print(player.name)
            # print("X: ",player.position_x,", Y: ",player.position_y)
            # time.sleep(10)
            self.game.new_episode()
            state = self.game.get_state()
            enemy = state.objects[0] if state.objects[0].name == "Cacodemon" else state.objects[1]
            player = state.objects[0] if state.objects[0].name == "DoomPlayer" else state.objects[1]
            positions = (abs(enemy.position_y) - abs(player.position_y))
            # print("resta: ", positions)
        # cont = 0
        # if random.random() < 0.5:
        #     while (enemy.position_y > 50) and cont < 3:
        #         # if random.random() < 0.5:
        #         self.game.new_episode()
        #         cont+=1
        grayScaledImg = self.grayScale()
        return  grayScaledImg, {}

    def render(self,render):
        if render == True:
            self.game.set_window_visible(True)
            
        return self.reset()
    
    def reset2(
        self,
        *,
        seed: Optional[int] = None,
        options: Optional[dict] = None,
        cont
    ):
        super().reset(seed=seed)
        # if seed is not None:
        #     self.game.set_seed(seed)
        self.game.new_episode()
        # self.game.new_episode()
        state = self.game.get_state()
        enemy = state.objects[0] if state.objects[0].name == "Cacodemon" else state.objects[1]
        player = state.objects[0] if state.objects[0].name == "DoomPlayer" else state.objects[1]
        positions = (abs(enemy.position_y) - abs(player.position_y))
        # print("resta: ", positions)
        # print(enemy.name)
        # print("X: ",enemy.position_x,", Y: ",enemy.position_y)
        # print(player.name)
        # print("X: ",player.position_x,", Y: ",player.position_y)
        while positions > (-30) and positions < 30: #if the enemy is too close to the player
            # print("resta: ", positions)
            # print(enemy.name)
            # print("X: ",enemy.position_x,", Y: ",enemy.position_y)
            # print(player.name)
            # print("X: ",player.position_x,", Y: ",player.position_y)
            self.game.new_episode()
            state = self.game.get_state()
            enemy = state.objects[0] if state.objects[0].name == "Cacodemon" else state.objects[1]
            player = state.objects[0] if state.objects[0].name == "DoomPlayer" else state.objects[1]
            positions = (abs(enemy.position_y) - abs(player.position_y))
        # cont = 0
        # if random.random() < 0.5:
        #     while (enemy.position_y > 50) and cont < 3:
        #         # if random.random() < 0.5:
        #         self.game.new_episode()
        #         cont+=1
        grayScaledImg = self.grayScale()
        return  grayScaledImg, {}
        
    def get_total_reward(self):
        return self.game.get_total_reward()
    
    def close(self):
        self.game.close()