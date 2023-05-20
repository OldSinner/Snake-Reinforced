import pygame
from Game import Snake
pygame.init()

game = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    game.draw()


pygame.quit()
