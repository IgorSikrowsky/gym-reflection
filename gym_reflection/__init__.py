import logging
from gym.envs.registration import register

name = 'gym-reflection'
logger = logging.getLogger(__name__)

register(
    id='reflection-v0',
    entry_point='gym_reflection.envs.ReflectionEnv',
    reward_threshold=1.0,
)