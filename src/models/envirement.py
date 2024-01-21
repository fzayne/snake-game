from models.snakeModel import Snake
from models.appleModel import Apple
from viw.game_over import game_over
from viw.score import draw_Score
import numpy as np
import pygame

class Envirement:
    def reset(self):
        self.snake= Snake()
        self.apple = Apple()
        self.direction="RIGHT"
        self.score=0

    def updateUI(self,screen):
        screen.fill((0,0,0))
        draw_Score(self.score,screen)
        self.snake.draw_snake(screen)
        self.apple.drawApple(screen)
        pygame.display.flip()
    def step(self,action):
        directions=["RIGHT","DOWN","LEFT","UP"]
        idx=directions.index(self.direction)
        if np.array_equal(action,[1,0,0]):
            self.direction=directions[idx]
        elif np.array_equal(action,[0,1,0]):
            self.direction=directions[(idx+1)%4]
        else:
            self.direction=directions[(idx-1)%4]
        self.snake.update(self.direction)
        if self.snake.snake_position[0]==self.apple.position[0] and self.snake.snake_position[1]==self.apple.position[1]:
            self.score += 1
            self.apple.__init__()
            
        else:
            self.snake.snake_body.pop()
        if self.snake.collision():
            game_over(self.score,self.screen)