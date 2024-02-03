import gymnasium as gym
import bandits
import numpy as np

env = gym.make("bandits/TwoArmedBanditEnv", use_fixed_values=False)
observation, info = env.reset(seed=42)
actions = env.action_space.n
shape = env.observation_space

totalReward = 0
terminated = False

for i in range(10):
   while terminated is False:
      action = env.action_space.sample()  # this is where you would insert your policy

      observation, reward, terminated, truncated, info = env.step(action)

      if terminated or truncated:
         print(info)
         env.reset()
         break
   terminated = False


