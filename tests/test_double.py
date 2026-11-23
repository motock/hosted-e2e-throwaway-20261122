import pytest

from tinycalc import double


def test_double_doubles_a_positive_number():
    assert double(4) == 8


def test_double_doubles_a_negative_number():
    assert double(-3) == -6


def test_double_of_zero_is_zero():
    assert double(0) == 0


def test_double_rejects_none():
    with pytest.raises(TypeError):
        double(None)
