import pygame
from Game import Snake
pygame.init()

game = Snake()

while True:
    game.make_step()


pygame.quit()
