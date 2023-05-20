import pygame
from Const import *
from Math import Point


class Snake:
    def __init__(self):
        # Screen
        self.w = SCREEN_WIDTH
        self.h = SCREEN_HEIGHT
        self.display = pygame.display.set_mode((self.w, self.h))
        self.max_x = self.w / BLOCK_SIZE
        self.max_y = self.h / BLOCK_SIZE
        pygame.display.set_caption("Snake")

        # Game Time
        self.clock = pygame.time.Clock()

    def draw(self):
        self.display.fill(Colors.BLACK.value)
        draw_rect_on_screen(self.display, Colors.RED.value, Point(0, 0))
        draw_rect_on_screen(self.display, Colors.RED.value, Point(1, 1))
        draw_rect_on_screen(self.display, Colors.RED.value, Point(2, 2))

        pygame.display.flip()


def draw_rect_on_screen(display, color, point):
    rect = pygame.Rect(point.x * BLOCK_SIZE, point.y *
                       BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(display, color, rect)
