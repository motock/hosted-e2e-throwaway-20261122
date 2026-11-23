import pytest

from tinycalc import negate


def test_negate_returns_the_negative_of_a_positive_number():
    assert negate(3) == -3


def test_negate_returns_the_positive_of_a_negative_number():
    assert negate(-2) == 2


def test_negate_of_zero_is_zero():
    assert negate(0) == 0


def test_negate_rejects_none():
    with pytest.raises(TypeError):
        negate(None)
