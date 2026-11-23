import pytest

from tinycalc import triple


def test_triple_triples_a_positive_number():
    assert triple(4) == 12


def test_triple_triples_a_negative_number():
    assert triple(-3) == -9


def test_triple_of_zero_is_zero():
    assert triple(0) == 0


def test_triple_rejects_none():
    with pytest.raises(TypeError):
        triple(None)
