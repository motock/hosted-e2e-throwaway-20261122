import pytest

from tinycalc import absolute


def test_absolute_returns_positive_value_unchanged():
    assert absolute(3) == 3


def test_absolute_returns_magnitude_of_negative_value():
    assert absolute(-2) == 2


def test_absolute_of_zero_is_zero():
    assert absolute(0) == 0


def test_absolute_rejects_none():
    with pytest.raises(TypeError):
        absolute(None)
