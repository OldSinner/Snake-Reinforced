import pygame
from Game import Snake

if __name__ == '__main__':
    game = Snake()

    while True:
        print(game.make_step([0, 1, 0]))
    pygame.quit()