from enum import Enum


class Colors(Enum):
    WHITE = (255, 255, 255)
    RED = (200, 0, 0)
    BLUE = (0, 0, 22)
    BLACK = (0, 0, 0)


class GameConst(Enum):
    BLOCK_SIZE = 20


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
