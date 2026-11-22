import pytest

from tinycalc import multiply


def test_multiply_returns_the_product():
    assert multiply(4, 3) == 12


def test_multiply_handles_negative_operands():
    assert multiply(-2, 5) == -10


def test_multiply_by_zero_returns_zero():
    assert multiply(0, 7) == 0


def test_multiply_rejects_none_operand():
    with pytest.raises(TypeError):
        multiply(None, 2)
