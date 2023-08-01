from typing import Iterable

def replace_last(numbers) -> Iterable:
    return numbers[-1:] + numbers[:-1]
