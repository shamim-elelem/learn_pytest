import pytest 


def multipley(a, b):
    return a * b

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (4, 5, 20),
    (0, 10, 0),
    (-1, 5, -5),
])
def test_multiply(a, b, expected):
    assert multipley(a, b) == expected