from gymnasium.envs.registration import register

register(
    id="bandits/TwoArmedBanditEnv",
    entry_point="bandits.envs:TwoArmedBanditEnv",
)
