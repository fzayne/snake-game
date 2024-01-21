import random
import numpy as np
from collections import deque
from models.envirement import Envirement

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:
    def __init__(self) -> None:
        self.n_games=0
        self.epsilon=0
        self.gamma=0.9
        self.memory= deque(maxlen=MAX_MEMORY)

    def get_state(self,env):
        point_r=(env.snake.position[0]+20,env.snake.position[1])
        point_l=(env.snake.position[0]-20,env.snake.position[1])
        point_u=(env.snake.position[0],env.snake.position[1]-20)
        point_d=(env.snake.position[0],env.snake.position[1]+20)

        dir_r= env.direction == "RIGHT"
        dir_l= env.direction == "LEFT"
        dir_u= env.direction == "UP"
        dir_d= env.direction == "DOWN"

        state=[
            (dir_r and env.snake.collision(point_r)) or
            (dir_l and env.snake.collision(point_l)) or
            (dir_u and env.snake.collision(point_u)) or
            (dir_d and env.snake.collision(point_d)),

            (dir_r and env.snake.collision(point_d)) or  
            (dir_d and env.snake.collision(point_l)) or  
            (dir_l and env.snake.collision(point_u)) or  
            (dir_u and env.snake.collision(point_r)) ,

            (dir_r and env.snake.collision(point_u)) or  
            (dir_u and env.snake.collision(point_l)) or  
            (dir_l and env.snake.collision(point_d)) or  
            (dir_d and env.snake.collision(point_r)) ,

            dir_l,
            dir_r,
            dir_u,
            dir_d,

            (env.apple.position[1]< env.snake.position[1]),
            (env.apple.position[1]> env.snake.position[1]),
            (env.apple.position[0]< env.snake.position[0]),
            (env.apple.position[0]> env.snake.position[0]),


        ]
        return np.array(state,dtype=int)
        
    def get_action():
        pass
    def rember():
        pass
    def train_short_memory():
        pass
    def train_long_memory():
        pass
