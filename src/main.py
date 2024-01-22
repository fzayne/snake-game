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
from models.agent import Agent
from ploter import plot

pygame.init()
running=True
plot_scores=[]
plot_mean_score=[]
total_score=0
record=0
agent=Agent()
env=Envirement()
env.reset()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
    state_old=agent.get_state(env)
    final_move=agent.get_action(state_old)

   
    print(env.step(final_move))
    reward, done, score= env.step(final_move)
    env.updateUI()
    state_new=agent.get_state(env)
    agent.train_short_memory(state_old, final_move, reward, state_new, done)
    agent.rember(state_old, final_move, reward, state_new, done)
    if done:
        env.reset()
        agent.n_games+=1
        agent.train_long_memory()

        if score > record:
            record=score
            agent.model.save()
        plot_scores.append(score)
        total_score += score
        plot_mean_score.append((total_score/agent.n_games))
        plot(plot_scores,plot_mean_score)
    

pygame.quit()