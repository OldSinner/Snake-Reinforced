import pygame
import random
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

    def make_step(self):
        self.handle_input()
        self.move()
        self.draw()
        self.check_game_status()
        self.clock.tick(SPEED)

        if self.gameover:
            self.start_newgame()

    def check_game_status(self):
        if self.is_collide():
            self.gameover = True
    
    def create_food(self):
        x = random.randint(0, self.max_x - 1)
        y = random.randint(0, self.max_y - 1)
        self.food = Point(x, y)
        while self.food in self.snake:
            self.create_food()
        self.food = Point(x, y)

    def draw(self):
        self.display.fill(Colors.BLACK.value)
        text_surface = self.score_counter.render("Score: "+str(self.score), True, Colors.WHITE.value)
        self.display.blit(text_surface, (0,0))
        for point in self.snake:
            draw_rect_on_screen(self.display, Colors.BLUE.value, point)
        draw_rect_on_screen(self.display, Colors.RED.value, self.food)
        pygame.display.flip()

    def is_collide(self):
        if self.snake_head.x < 0 or self.snake_head.x > self.max_x - 1 or self.snake_head.y < 0 or self.snake_head.y > self.max_y - 1:
            return True
        if self.snake_head in self.snake[1:]:
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

        if self.is_get_food() == False:
            self.snake.pop()

    def is_get_food(self):
        if self.snake_head == self.food:
            self.score += 1
            self.create_food()
            return True
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
