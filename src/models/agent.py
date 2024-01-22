import random
import numpy as np
from collections import deque
from models.model import Linear_QNet,Qtrainer
import torch

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:
    def __init__(self) -> None:
        self.n_games=0
        self.epsilon=0
        self.gamma=0.9
        self.memory= deque(maxlen=MAX_MEMORY)
        self.model=Linear_QNet(11,512,3)
        self.trainer=Qtrainer(self.model,lr=LR,gamma=self.gamma)

    def get_state(self,env):
        point_r=(env.snake.snake_position[0]+20,env.snake.snake_position[1])
        point_l=(env.snake.snake_position[0]-20,env.snake.snake_position[1])
        point_u=(env.snake.snake_position[0],env.snake.snake_position[1]-20)
        point_d=(env.snake.snake_position[0],env.snake.snake_position[1]+20)

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

            (env.apple.position[1]< env.snake.snake_position[1]),
            (env.apple.position[1]> env.snake.snake_position[1]),
            (env.apple.position[0]< env.snake.snake_position[0]),
            (env.apple.position[0]> env.snake.snake_position[0]),


        ]
        return np.array(state,dtype=int)
        
    def get_action(self,state):
        self.epsilon = 80-self.n_games
        final_move=[0,0,0]
        if random.randint(0,200) < self.epsilon:
            move=random.randint(0,2)
            final_move[move]=1
        else:
            state0=torch.tensor(state,dtype=torch.float)
            prediction=self.model(state0)
            move=torch.argmax(prediction).item()
            final_move[move]=1
        return final_move
    
    def rember(self,state,action,reward,next_state,done):
       self.memory.append((state,action,reward,next_state,done)) 
    
    def train_short_memory(self,state,action,reward,next_state,done):
       self.trainer.train_step(state,action,reward,next_state,done) 

    def train_long_memory(self):
        if len(self.memory) >BATCH_SIZE:
            mini_sample=random.sample(self.memory,BATCH_SIZE)
        else:
            mini_sample=self.memory
        states,actions,rewards,next_states,dones=zip(*mini_sample)
        self.trainer.train_step(states,actions,rewards,next_states,dones)
