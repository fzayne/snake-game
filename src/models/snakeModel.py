import pygame
from time import sleep
from data import BLOCK_SIZE,speed,SCREEN_HEIGHT,SCREEN_WIDTH

class Snake(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super(Snake,self).__init__()
        # self.surf=pygame.Surface((BLOCK_SIZE,BLOCK_SIZE))
        self.snake_body=[[0,80],[0,60],[0,40]]
        self.snake_position=[0,80]
        # self.surf.fill((0,255,0))
        # self.rect=self.surf.get_rect()

    def draw_snake(self,surface):
        for body in self.snake_body:
            pygame.draw.rect(surface,(0,255,0),pygame.Rect(body[0],body[1],BLOCK_SIZE,BLOCK_SIZE))

    def update(self,direction):
        sleep(0.1)
        if direction=="UP":
            self.snake_position[1] -= speed
            # self.rect.move_ip(0, -speed)

        if direction=="DOWN":
            self.snake_position[1] += speed
            # self.rect.move_ip(0, speed)

        if direction=="RIGHT":
            self.snake_position[0] += speed
            # self.rect.move_ip(speed, 0)
            # self.surf.scroll(speed, 0)
        if direction=="LEFT":
            self.snake_position[0] -= speed
            # self.rect.move_ip(-speed, 0)
            #  self.surf.scroll(-speed, 0)

        self.snake_body.insert(0,list(self.snake_position))

    
    def collision(self):
        if self.snake_position[0] < 0 or self.snake_position[0] > SCREEN_HEIGHT or self.snake_position[1] < 0 or self.snake_position[1] > SCREEN_WIDTH:
            return True
        for pos in self.snake_body[1:]:
            if pos == self.snake_position:
                return True
        return False
        