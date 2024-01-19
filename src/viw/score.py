import pygame


def draw_Score(score,screen):
    score_font = pygame.font.SysFont("None", 45)
    score_surface = score_font.render('Score : ' + str(score), True, (255,255,255))
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)