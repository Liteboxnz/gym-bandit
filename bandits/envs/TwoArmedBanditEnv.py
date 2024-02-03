import gymnasium as gym
from gymnasium import spaces
import random

class TwoArmedBanditEnv(gym.Env):

    def __init__(self, fixed_var=3, fixed_var_2=7, runs=100, use_fixed_values=True):

        if use_fixed_values:
            self.fixed_var = fixed_var
            self.fixed_var_2 = fixed_var_2
        else:
            self.fixed_var = random.randint(1, 10)
            self.fixed_var_2 = random.randint(1, 10)

        self.max_runs = runs

        # easy tracking
        self.total_reward = 0
        self.run_counter = 0

        # No state (note 0 indexed)
        self.observation_space = spaces.Discrete(1)

        # Output (0-10) should be the outcome of the choice
       # self.observation_space = spaces.Dict({"total_reward": spaces.Discrete(100)})

       # self.observation_space.sample()

        # We have 2 options/bandits here [0,1]
        self.action_space = spaces.Discrete(2)
        self.render_mode = None
        self.window = None
        self.clock = None

    def _get_obs(self):
        return 0
        #return {"total_reward": self.total_reward}

    # average award etc? debug info?
    def _get_info(self):
        return {"total_reward": self.total_reward}

    def reset(self, seed=None, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)

        observation = self._get_obs()
        info = self._get_info()

        return observation, info

    def step(self, action):

        if action == 0:
            reward = self.fixed_var
        else:
            reward = self.fixed_var_2

        self.total_reward += reward

        terminated = self.run_counter > self.max_runs
        observation = self._get_obs()
        info = self._get_info()

        self.run_counter += 1

        return observation, reward, terminated, False, info