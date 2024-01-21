import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from models.envirement import Envirement

pygame.init()
screen=pygame.display.set_mode((500,500))
running=True

env=Envirement()
env.reset()
while running:
    
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                if env.direction!="DOWN":
                    env.direction="UP"
            if event.key == K_DOWN:
                if env.direction!="UP":
                    env.direction="DOWN"
            if event.key == K_RIGHT:
                if env.direction!="LEFT":
                    env.direction="RIGHT"
            if event.key == K_LEFT:
                if env.direction!="RIGHT":
                    env.direction="LEFT"
    env.step()
    env.updateUI(screen)

    

pygame.quit()