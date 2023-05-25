import pygame
import random
import numpy as np
from Const import *
from Math import Point


class Snake:
    def __init__(self):
        self.reward = None
        pygame.init()
        pygame.font.init()
        # Screen
        self.w = SCREEN_WIDTH
        self.h = SCREEN_HEIGHT
        self.display = pygame.display.set_mode((self.w, self.h))
        self.max_x = self.w / BLOCK_SIZE
        self.max_y = self.h / BLOCK_SIZE
        pygame.display.set_caption("Snake")
        self.step_counter = 0;

        # Game logic
        self.clock = pygame.time.Clock()
        self.start_newgame()
        self.score_counter = pygame.font.SysFont('Arial', 20)

    def start_newgame(self):
        self.score = 0
        self.gameover = False
        self.snake_head = Point(self.max_x / 2, self.max_y / 2)
        self.snake = [self.snake_head, Point(
            self.snake_head.x - 1, self.snake_head.y), Point(self.snake_head.x - 2, self.snake_head.y)]
        self.direction = Direction.RIGHT
        self.create_food()

    def make_step(self, action):
        # Action Data From Game
        self.reward = 0
        self.step_counter += 1

        self.handle_input(action)
        if not self.gameover:
            self.move()
        self.draw()
        self.check_game_status()
        self.clock.tick(SPEED)

        return self.gameover, self.score, self.reward

    def check_game_status(self):
        if self.is_collide(self.snake_head) or self.step_counter > 100 * len(self.snake):
            self.gameover = True
            self.reward = -10

    def create_food(self):
        x = random.randint(0, self.max_x - 1)
        y = random.randint(0, self.max_y - 1)
        self.food = Point(x, y)
        while self.food in self.snake:
            self.create_food()
        self.food = Point(x, y)

    def draw(self):
        self.display.fill(Colors.BLACK.value)
        text_surface = self.score_counter.render("Score: " + str(self.score), True, Colors.WHITE.value)
        self.display.blit(text_surface, (0, 0))
        for point in self.snake:
            draw_rect_on_screen(self.display, Colors.BLUE.value, point)
        draw_rect_on_screen(self.display, Colors.RED.value, self.food)
        pygame.display.flip()

    def is_collide(self, pt):
        if pt.x < 0 or pt.x > self.max_x - 1 or pt.y < 0 or pt.y > self.max_y - 1:
            return True
        if pt in self.snake[1:]:
            return True
        return False

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

        self.snake_head = Point(x, y)
        self.snake.insert(0, self.snake_head)
        if not self.is_get_food():
            self.snake.pop()

    def is_get_food(self):
        if self.snake_head == self.food:
            self.score += 1
            self.reward = 10
            self.create_food()
            return True
        return False

    def handle_input(self, action):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        directions = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
        idx = directions.index(self.direction)
        if action[1] == 1:
            idx = (idx + 1) % 4
        elif action[2] == 1:
            idx = (idx - 1) % 4
        self.direction = directions[idx]

    def create_state(self):
        head = self.snake_head

        point_l = Point(head.x - 1, head.y)
        point_r = Point(head.x + 1, head.y)
        point_u = Point(head.x, head.y - 1)
        point_d = Point(head.x, head.y + 1)

        dir_l = self.direction == Direction.LEFT
        dir_r = self.direction == Direction.RIGHT
        dir_u = self.direction == Direction.UP
        dir_d = self.direction == Direction.DOWN

        state = [
            # Danger straight
            (dir_r and self.is_collide(point_r)) or
            (dir_l and self.is_collide(point_l)) or
            (dir_u and self.is_collide(point_u)) or
            (dir_d and self.is_collide(point_d)),

            # Danger right
            (dir_u and self.is_collide(point_r)) or
            (dir_d and self.is_collide(point_l)) or
            (dir_l and self.is_collide(point_u)) or
            (dir_r and self.is_collide(point_d)),

            # Danger left
            (dir_d and self.is_collide(point_r)) or
            (dir_u and self.is_collide(point_l)) or
            (dir_r and self.is_collide(point_u)) or
            (dir_l and self.is_collide(point_d)),

            # Move direction
            dir_l,
            dir_r,
            dir_u,
            dir_d,

            # Food location 
            self.food.x < self.snake_head.x,  # food left
            self.food.x > self.snake_head.x,  # food right
            self.food.y < self.snake_head.y,  # food up
            self.food.y > self.snake_head.y  # food down
        ]

        return np.array(state, dtype=int)


def draw_rect_on_screen(display, color, point):
    rect = pygame.Rect(point.x * BLOCK_SIZE, point.y *
                       BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(display, color, rect)
