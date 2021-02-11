import random
from typing import Tuple, Union, List

import pygame

from model import Snake, Square

IntTuple = Tuple[int, int]
Model = Union[Snake, Square]


class Board:

    def __init__(self, size: IntTuple, step: int, offset: int):
        self.step = step
        self.offset = offset
        self.rows = (size[0] + offset) // (step + offset)
        self.columns = (size[1] + offset) // (step + offset)
        self.size = _compute_size(self.rows, self.columns, step, offset)
        self.screen = pygame.display.set_mode(self.size)

    def _compute_position(self, square: Square) -> IntTuple:
        x = self.step + (square.row - 1) * (self.step + self.offset)
        y = self.step + (square.column - 1) * (self.step + self.offset)
        return x, y

    @property
    def start(self):
        return self.rows // 2, self.columns // 2

    @property
    def squares(self):
        rows, columns = range(0, self.rows), range(0, self.columns)
        return [Square(row, column) for row, column in zip(rows, columns)]

    def fill(self, color='black'):
        self.screen.fill(color)

    def draw(self, model: Model, color='white') -> None:
        if isinstance(model, Snake):
            for square in model:
                self._draw_square(square, color)
        if isinstance(model, Square):
            self._draw_square(model, color)

    def _draw_square(self, square: Square, color='white') -> None:
        position = self._compute_position(square)
        size = (self.step, self.step)
        pygame.draw.rect(self.screen, color, (position, size))


def _compute_size(rows: int, columns: int, step: int, offset: int) -> IntTuple:
    x = step + (rows - 1) * (step + offset)
    y = step + (columns - 1) * (step + offset)
    return x, y


def random_food(board: Board, exclude: List[Square] = None):
    squares = _filtered_squares(board.squares, exclude) if exclude else board.squares
    return random.choice(squares)


def _filtered_squares(positions: List[Square], exclude: List[Square]) -> List[Square]:
    positions = set(square.position for square in positions)
    excluded = set(square.position for square in exclude)
    return [Square(*position) for position in positions.difference(excluded)]
