from typing import Tuple


def tuple_converter(string: str) -> Tuple[int, ...]:
    string = string.strip('()')
    values = map(int, string.split(', '))
    return tuple(values)


def compute_coordinate(limit: int, step: int, offset: int) -> int:
    r = step + offset
    n = (limit - step + r) // r
    return step + (n - 1) * r
