from typing import Tuple

from pygame import Vector2


def tuple_converter(string: str) -> Tuple[int, ...]:
    string = string.strip('()')
    values = map(int, string.split(', '))
    return tuple(values)


def compute_coordinate(limit: int, step: int, offset: int) -> int:
    r = step + offset
    n = (limit - step + r) // r
    return step + (n - 1) * r


def scale_vector(vector: Vector2, scalar: int) -> Vector2:
    return Vector2(vector[0] * scalar, vector[1] * scalar)