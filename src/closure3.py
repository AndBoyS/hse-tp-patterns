from collections.abc import Callable


def cache(func: Callable[[int, int], int]) -> Callable[[int, int], int]:
    _cache: dict[tuple[int, int], int] = {}

    def new_func(x: int, y: int):
        if (x, y) in _cache:
            return _cache[(x, y)]
        res = func(x, y)
        _cache[(x, y)] = res
        return res

    return new_func


@cache
def sum(x, y) -> int:
    return x + y


sum(1, 2)
sum(2, 2)
sum(1, 2)
