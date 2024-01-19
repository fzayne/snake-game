import pygame
from data import BLOCK_SIZE,SCREEN_WIDTH,SCREEN_HEIGHT
import random

class Apple:
    def __init__(self) -> None:
        super(Apple,self).__init__()
        self.position=[random.randrange(1,(SCREEN_WIDTH//BLOCK_SIZE))*BLOCK_SIZE,random.randrange(1,(SCREEN_HEIGHT//BLOCK_SIZE))*BLOCK_SIZE]

    def drawApple(self,screen):
        pygame.draw.rect(screen,(255,0,0),pygame.Rect(self.position[0],self.position[1],BLOCK_SIZE,BLOCK_SIZE))

       