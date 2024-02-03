import gymnasium as gym
from gymnasium import spaces


class TwoArmedBanditEnv(gym.Env):

    def __init__(self, fixed_var=3, fixed_var_2=7, runs=100):
        self.fixed_var = fixed_var
        self.fixed_var_2 = fixed_var_2
        self.max_runs = runs

        # easy tracking
        self.total_reward = 0
        self.run_counter = 0

        # Output (0-10) should be the outcome of the choice
        self.observation_space = spaces.Dict({"total_reward": spaces.Discrete(10)})

        self.observation_space.sample()

        # We have 2 options/bandits here [0,1]
        self.action_space = spaces.Discrete(2)
        self.render_mode = None
        self.window = None
        self.clock = None

    def _get_obs(self):
        return {"total_reward": self.total_reward}

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
        print(observation)
        info = self._get_info()

        self.run_counter += 1

        return observation, reward, terminated, False, info
