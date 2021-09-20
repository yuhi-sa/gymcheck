import gym
import pybullet_envs

from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import VecVideoRecorder, DummyVecEnv


def make_video(name, ENV_ID, video_length, IS_LEARN, learn_episode):
  video_folder = "./data/"+ name + "/videos/"
  env = DummyVecEnv([lambda: gym.make(ENV_ID)])
  obs = env.reset()

  if IS_LEARN:
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=learn_episode)

    env = VecVideoRecorder(env, video_folder,
                          record_video_trigger=lambda x: x == 0, video_length=video_length,
                          name_prefix="learned-agent-{}".format(name))

    obs = env.reset()
    for _ in range(video_length+1):
        env.render()
        action, states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
        if done:
          break
    env.close()

  else:
    env = VecVideoRecorder(env, video_folder,
                          record_video_trigger=lambda x: x == 0, video_length=video_length,
                          name_prefix="random-agent-{}".format(name))
    obs = env.reset()
    for _ in range(video_length + 1):
      env.render()
      action = [env.action_space.sample()]
      obs, rewards, done, info = env.step(action)
      if done:
          break
    env.close()