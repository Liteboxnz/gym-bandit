# gym-bandit
Some bandit algorithms for gymnasium

### TwoArmedBanditEnv

This is a tiny, getting started environment

### Usage:
In the folder install the package to pip
```pip install -e .```

```
import gymnasium as gym
import bandits

env = gym.make("bandits/TwoArmedBanditEnv")


for _ in range(10000):
   action = env.action_space.sample()  # this is where you would insert your policy

   observation, reward, terminated, truncated, info = env.step(action)

   totalReward=totalReward+reward

   if terminated or truncated:
      print(totalReward)
      env.close()
      break
```
