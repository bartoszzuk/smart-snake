from typing import Tuple


def tuple_converter(string: str) -> Tuple[int, ...]:
    string = string.strip('()')
    values = map(int, string.split(', '))
    return tuple(values)
