from typing import Generic, TypeVar

T = TypeVar('T')

def TODO() -> None:
    raise NotImplementedError("TODO")

def MISSING_IMPLEMENTATION() -> None:
    raise NotImplementedError("This method is not implemented")

class OneOrMore(Generic[T]): ...