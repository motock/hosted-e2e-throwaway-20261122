"""A tiny calculator used as a throwaway pipeline test target."""


def add(left: float, right: float) -> float:
    """Return the sum of two numbers."""
    return left + right


def square(value):
    """Return value squared."""
    return value * value


def absolute(value: float) -> float:
    """Return the absolute value of a number."""
    return abs(value)


def negate(value: float) -> float:
    """Return the additive inverse of a number."""
    return -value
