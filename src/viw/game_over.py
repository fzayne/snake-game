import time
import pygame
from data import SCREEN_WIDTH,SCREEN_HEIGHT

def game_over(score,game_window):
   
    
    my_font = pygame.font.SysFont('times new roman', 50)
     
   
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, (255,0,0))
     
    
    game_over_rect = game_over_surface.get_rect()
     
   
    game_over_rect.midtop = (SCREEN_WIDTH/2, SCREEN_HEIGHT/4)
     
   
    game_window.blit(game_over_surface, game_over_rect)

    pygame.display.flip()
     
    
    time.sleep(2)
     
   
    pygame.quit()
     
    
    quit()