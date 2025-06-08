from collections.abc import Iterable, Sequence, Sized


def describe_size(obj: Sized) -> str:
    return f"Object has size {len(obj)}"


def squared_sum(it: Iterable[int]) -> int:
    return sum(el**2 for el in it)


def last_element(seq: Sequence[int]) -> int:
    return seq[-1]
