import pytest

from tinycalc import square


def test_square_positive():
    assert square(4) == 16


def test_square_negative():
    assert square(-3) == 9


def test_square_zero():
    assert square(0) == 0


def test_square_none_raises_typeerror():
    with pytest.raises(TypeError):
        square(None)
