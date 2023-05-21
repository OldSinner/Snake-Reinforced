from enum import Enum
BLOCK_SIZE = 20
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SPEED = 10

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
