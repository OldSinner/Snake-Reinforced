import pygame
from Game import Snake
pygame.init()
pygame.font.init()

game = Snake()

while True:
    print(game.make_step([0,1,0]))
pygame.quit()
