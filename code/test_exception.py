import pytest

def add_one(x):
    if x <= 0:
        raise ValueError("positive value expected")
    else:
        return x + 1

def test_add_one():
    assert add_one(3) == 4

    with pytest.raises(ValueError):
        add_one(-1)
