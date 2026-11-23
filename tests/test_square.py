import pytest
from tinycalc import square

def test_square_three():    assert square(3) == 9
def test_square_negative(): assert square(-2) == 4
def test_square_zero():     assert square(0) == 0
def test_square_none_raises():
    with pytest.raises(TypeError):
        square(None)
