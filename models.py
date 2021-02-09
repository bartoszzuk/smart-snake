import random
from collections import deque
from enum import Enum
from typing import List

import utils
import pygame
from dataclasses import dataclass
from pygame import Vector2, Surface


class Direction(Enum):
    UP = Vector2(0, -1)
    DOWN = Vector2(0, 1)
    LEFT = Vector2(-1, 0)
    RIGHT = Vector2(1, 0)

    def opposite(self):
        return utils.scale_vector(self.value, -1)


@dataclass
class Square:
    position: Vector2
    size: Vector2

    def draw(self, screen: Surface, color='red'):
        pygame.draw.rect(screen, color, (self.position, self.size))


class Snake:

    def __init__(self, start: Vector2, step=20, offset=2, length=4):
        self.step = step
        self.offset = offset
        self.size = Vector2(step, step)
        self.squares = self._squares(start, length)
        self.directions = deque([Direction.UP] * length)

    def _squares(self, start: Vector2, length: int) -> List[Square]:
        square = []
        for index in range(length):
            position = Vector2(start[0], index * (self.step + self.offset) + start[1])
            square.append(Square(position, self.size))
        return square

    @property
    def head(self) -> Square:
        return self.squares[0]

    def move(self, direction: Direction):
        self.directions.appendleft(direction)
        self.directions.pop()
        for square, direction in zip(self.squares, self.directions):
            step = self.step + self.offset
            move = utils.scale_vector(direction.value, step)
            square.position += move

    def grow(self):
        direction = self.directions[-1]
        move = utils.scale_vector(direction.opposite(), self.step + self.offset)
        tail = Square(self.squares[-1].position + move, self.size)
        self.squares.append(tail)
        self.directions.append(direction)

    def draw(self, screen: Surface, color='red'):
        for square in self.squares:
            square.draw(screen, color)


# TODO test recursion and clean function
def random_food(screen: Surface, snake: Snake, step: int, offset: int) -> Square:
    size = screen.get_size()
    x = utils.compute_coordinate(random.randint(0, size[0]), step, offset)
    y = utils.compute_coordinate(random.randint(0, size[1]), step, offset)
    food = Square(Vector2(x, y), Vector2(step, step))
    return food if food.position not in [square.position for square in snake.squares] \
        else random_food(screen, snake, step, offset)

