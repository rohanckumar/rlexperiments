from spinup import ppo_tf1 as ppo
import tensorflow as tf
import gym

env_fn = lambda : gym.make('LunarLander-v2')

print(env_fn)

ac_kwargs = dict(hidden_sizes=[64,64], activation=tf.nn.relu)

logger_kwargs = dict(output_dir='result/test2', exp_name='experiment_name')

ppo(env_fn=env_fn, ac_kwargs=ac_kwargs, steps_per_epoch=5000, epochs=10, logger_kwargs=logger_kwargs)