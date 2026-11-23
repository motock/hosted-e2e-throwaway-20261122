import pytest

from tinycalc import quadruple


def test_quadruple_quadruples_a_positive_number():
    assert quadruple(4) == 16


def test_quadruple_quadruples_a_negative_number():
    assert quadruple(-3) == -12


def test_quadruple_of_zero_is_zero():
    assert quadruple(0) == 0


def test_quadruple_rejects_none():
    with pytest.raises(TypeError):
        quadruple(None)
