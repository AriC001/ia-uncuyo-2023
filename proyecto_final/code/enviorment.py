import gymnasium as gym
from gymnasium import spaces
# Import the OpenCV for image processing
import cv2
import numpy as np
import vizdoom as vzd
import time
from typing import Optional

class VizDoom(gym.Env):
    """Custom Environment that follows gym interface."""

    # metadata = {"render_modes": ["human"], "render_fps": 30}

    def __init__(self):
        super().__init__()
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
        self.game.set_episode_start_time(10)

        # Makes the window appear (turned on by default)
        self.game.set_window_visible(True)

        # Sets the living reward (for each move) to -1
        self.game.set_living_reward(-1)

        # In order to visualize depth buffer, you need to enable it first
        self.game.set_depth_buffer_enabled(True)

        # Initialize the game. Further configuration won't take any effect from now on.
        self.game.init()

        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(3)
        # Example for using image as input (channel-first; channel-last also works):
        self.observation_space = spaces.Box(low=0, high=255, shape=(480, 640,1), dtype=np.uint8)

    def step(self, action):
        #actions = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        #actions[0]= Move Left | actions[1]= Move Right | actions[2]= Attack 
        actions = np.identity(3, dtype=np.uint8) # [[1,0,0],[0,1,0],[0,0,1]]
        # action = random.choice(actions) #randomly choose an action from the set of posible actions
        frameSkip = 1 #number of frames to skip
        reward = self.game.make_action(actions[action],frameSkip) #make an action and get the reward
        if self.game.get_state():
            state = self.game.get_state() #get the state of the game with the screen buffer and game variables
            img = state.screen_buffer #get the screen buffer, the image that is rendered of the game frame by frame in an array of pixels in RGB24 format
            grayscaledImg = state.depth_buffer #get the depth buffer, the image that is rendered of the game frame by frame in an array of pixels in 8-bit gray channel format
            # grayscaledImg = np.repeat(state.depth_buffer[...], repeats=2, axis=1)
            grayscaledImg = np.stack([grayscaledImg] * 1, axis=2)
            info = {"ammo": 0}
            info["ammo"] = state.game_variables[0]
        else:
            grayscaledImg = np.zeros(self.observation_space.shape)
            info = {"ammo": 0}
            # info["ammo"] = state.game_variables[0]
        truncated = False  # Truncation to be handled by the TimeLimit wrapper
        print("\treward:", reward, end=" ")
        time.sleep(0.02)
        return grayscaledImg, reward, self.game.is_episode_finished(), truncated,info

    # def reset(self,seed):
    #     self.game.new_episode()
    #     return self.game.get_state().depth_buffer
    def reset(
        self,
        *,
        seed: Optional[int] = None,
        options: Optional[dict] = None,
    ):
        super().reset(seed=seed)
        if seed is not None:
            self.game.set_seed(seed)
        self.game.new_episode()
        # depth = self.game.get_state().depth_buffer
        grayscaledImg = self.game.get_state().depth_buffer
        grayscaledImg = np.stack([grayscaledImg] * 1, axis=2)
        return  grayscaledImg, {}

    # def render(self):
    #     ...

    # def close(self):
    #     ...