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
from models import appleModel, snakeModel
from viw.score import draw_Score
from viw.game_over import game_over

pygame.init()
screen=pygame.display.set_mode((500,500))
running=True
snake= snakeModel.Snake()
apple = appleModel.Apple()
direction="RIGHT"
score=0

def eat():
    global score
    if snake.snake_position[0]==apple.position[0] and snake.snake_position[1]==apple.position[1]:
        score += 1
        apple.__init__()
        pass
    else:
        snake.snake_body.pop()

while running:
    screen.fill((0,0,0))
    draw_Score(score,screen)
    snake.draw_snake(screen)
    apple.drawApple(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                if direction!="DOWN":
                    direction="UP"
            if event.key == K_DOWN:
                if direction!="UP":
                    direction="DOWN"
            if event.key == K_RIGHT:
                if direction!="LEFT":
                    direction="RIGHT"
            if event.key == K_LEFT:
                if direction!="RIGHT":
                    direction="LEFT"
    # pressed_keys = pygame.key.get_pressed()
    # if pressed_keys[K_UP]:
    #     snake.update("UP")
    # if pressed_keys[K_DOWN]:
    #     snake.update("DOWN")
    # if pressed_keys[K_LEFT]:
    #     snake.update("RIGHT")
    # if pressed_keys[K_RIGHT]:
    #     snake.update("LEFT")
    snake.update(direction)
    eat()
    if snake.collision():
        game_over(score,screen)
    # print("position before blit :",snake.rect)
    # screen.blit(snake.surf,snake.rect)
    # print("position after blit",snake.rect)
    # screen.blit(apple.surf,apple.rect)
    pygame.display.flip()
    

pygame.quit()