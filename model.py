from collections import deque
from enum import Enum
from typing import List, Iterator, Iterable, Tuple

from dataclasses import dataclass

IntTuple = Tuple[int, int]


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    def opposite(self):
        value = self.value[0] * -1, self.value[1] * -1
        return Direction(value)


@dataclass
class Square:
    row: int
    column: int

    @property
    def position(self) -> IntTuple:
        return self.row, self.column


class Snake(Iterable[Square]):

    def __init__(self, start: IntTuple, length: int):
        self.squares = _create_squares(start, length)
        self.directions = deque([Direction.UP] * length)

    def __iter__(self) -> Iterator[Square]:
        return iter(self.squares)

    @property
    def head(self) -> Square:
        return self.squares[0]

    def move(self, direction: Direction) -> None:
        self.directions.appendleft(direction)
        self.directions.pop()
        for square, direction in zip(self.squares, self.directions):
            square.row += direction.value[0]
            square.column += direction.value[1]

    def grow(self) -> None:
        tail = self.squares[-1]
        opposite = self.directions[-1].opposite()
        row = tail.row + opposite.value[0]
        column = tail.column + opposite.value[1]
        self.squares.append(Square(row, column))
        self.directions.append(self.directions[-1])


def _create_squares(start: IntTuple, length: int) -> List[Square]:
    return [Square(start[0], index + start[1]) for index in range(length)]

