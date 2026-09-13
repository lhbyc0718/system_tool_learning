import pytest
from calc import add, sub, mul, div

def test_add():
    assert add(1, 2) == 3

def test_sub():
    assert sub(5, 3) == 2

def test_mul():
    assert mul(2, 3) == 6

def test_div():
    assert div(6, 2) == 3

def test_div_zero():
    with pytest.raises(ValueError):
        div(1, 0)
