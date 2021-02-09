import random
from utils import compute_coordinate
from collections import deque
from enum import Enum
from typing import List

import pygame
from dataclasses import dataclass
from pygame import Vector2, Surface


class Direction(Enum):
    UP = Vector2(0, -1)
    DOWN = Vector2(0, 1)
    LEFT = Vector2(-1, 0)
    RIGHT = Vector2(1, 0)


@dataclass
class Square:
    position: Vector2
    size: Vector2

    def draw(self, screen: Surface, color='red'):
        pygame.draw.rect(screen, color, (self.position, self.size))


def random_food(screen: Surface, step: int, offset: int):
    size = screen.get_size()
    x = compute_coordinate(random.randint(0, size[0]), step, offset)
    y = compute_coordinate(random.randint(0, size[1]), step, offset)
    return Square(Vector2(x, y), Vector2(step, step))


class Snake:

    def __init__(self, start: Vector2, step=20, offset=2, length=8):
        self.step = step
        self.offset = offset
        self.squares = self._squares(start, length)
        self.directions = deque([Direction.UP] * length)

    def _squares(self, start: Vector2, length: int) -> List[Square]:
        square = []
        for index in range(length):
            size = Vector2(self.step, self.step)
            position = Vector2(start[0], index * (self.step + self.offset) + start[1])
            square.append(Square(position, size))
        return square

    def move(self, direction: Direction):
        self.directions.appendleft(direction)
        self.directions.pop()
        for square, direction in zip(self.squares, self.directions):
            step = self.step + self.offset
            move = Vector2([value * step for value in direction.value])
            square.position += move

    def draw(self, screen: Surface, color='red'):
        for square in self.squares:
            square.draw(screen, color)
