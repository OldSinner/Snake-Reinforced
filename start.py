import pygame
from Game import Snake
pygame.init()
pygame.font.init()

game = Snake()

while True:
    game.make_step()


pygame.quit()
