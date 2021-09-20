import os
import gym
import sys
import gym
import numpy as np
import pybullet_envs
import time
from gym.spaces import *
os.environ['MKL_THREADING_LAYER'] = 'GNU'

def make_markdown(name, datalist): 
    path = "./data/"+"/README.md" 
    f = open(path, "a")
    f.writelines(datalist)
    f.close()

def print_spaces(label, space, datalist):
    if isinstance(space, Box):
        datalist.append("|次元数|"+ str(space.shape[0]) + "dim" +"|\n")
        datalist.append("|最小値|"+ str(space.low) +"|\n")
        datalist.append("|最大値|"+ str(space.high) +"|\n")
        datalist.append("|型|"+ str(space.dtype) +"|\n")
        datalist.append("|連続・非連続|連続値|\n")

    if isinstance(space, Discrete):
        datalist.append("|次元数|"+ str(space.shape[0]) +"|\n")
        datalist.append("|最小値|"+ str(space.low) +"|\n")
        datalist.append("|最大値|"+ str(space.high) +"|\n")
        datalist.append("|型|"+ str(space.dtype) +"|\n")
        datalist.append("|連続・非連続|非連続値|\n")
    return datalist

def make_table(datalist):
    datalist.append("|name|value|\n")
    datalist.append("| ---- | ---- |\n")
    return datalist

def check_env(name, ENV_ID):

    datalist = ["# "+ ENV_ID+ "\n"]
    datalist.append("デモ動画は[こちら](./" + name + ")\n")

    env = gym.make(ENV_ID)
    
    # 行動空間
    datalist.append("## 行動空間\n")
    datalist = make_table(datalist)
    datalist = print_spaces("行動空間", env.action_space, datalist)
    datalist.append("\n")
    # 状態空間
    datalist.append("## 状態空間\n")
    datalist = make_table(datalist)
    datalist = print_spaces("状態空間", env.observation_space, datalist)
    datalist.append("\n")
    # その他
    datalist.append("## その他\n")
    datalist = make_table(datalist)
    datalist.append("|報酬のレンジ|"+ str(env.reward_range) +"|\n") 
    datalist.append("|最大エピソード数|"+ str(env._max_episode_steps) +"|\n")
    datalist.append("\n")

    make_markdown(name, datalist)