from enum import Enum
# Game
BLOCK_SIZE = 20
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SPEED = 10
# Agent
MAX_MEMORY = 100_000
BATCH_SIZE = 1000

# AI
LR = 0.001

class Colors(Enum):
    WHITE = (255, 255, 255)
    RED = (200, 0, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
