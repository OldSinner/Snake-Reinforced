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

        # Snake
        self.snake_head = Point(self.max_x / 2, self.max_y / 2)
        self.snake = [self.snake_head, Point(
            self.snake_head.x - 1, self.snake_head.y), Point(self.snake_head.x - 2, self.snake_head.y)]
        self.direction = Direction.RIGHT

    def make_step(self):
        self.handle_input()
        self.move()
        self.draw()
        self.clock.tick(SPEED)

    def draw(self):
        self.display.fill(Colors.BLACK.value)
        for point in self.snake:
            draw_rect_on_screen(self.display, Colors.RED.value, point)
        pygame.display.flip()

    def move(self):
        x = self.snake_head.x
        y = self.snake_head.y
        if self.direction == Direction.RIGHT:
            x += 1
        elif self.direction == Direction.LEFT:
            x -= 1
        elif self.direction == Direction.UP:
            y -= 1
        elif self.direction == Direction.DOWN:
            y += 1

        if self.is_get_food() == False:
            self.snake.pop()

        self.snake_head = Point(x, y)
        self.snake.insert(0, self.snake_head)
        print(self.snake_head)

    def is_get_food(self):
        return False

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.direction = Direction.LEFT
            elif keys[pygame.K_RIGHT]:
                self.direction = Direction.RIGHT
            elif keys[pygame.K_UP]:
                self.direction = Direction.UP
            elif keys[pygame.K_DOWN]:
                self.direction = Direction.DOWN


def draw_rect_on_screen(display, color, point):
    rect = pygame.Rect(point.x * BLOCK_SIZE, point.y *
                       BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(display, color, rect)
