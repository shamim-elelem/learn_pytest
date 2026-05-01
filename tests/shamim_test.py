def subtract(a, b):
    """Simple subtraction function"""
    return a - b

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 1) == -1
    assert subtract(-1, -1) == 0
    assert subtract(3.5, 2.5) == 1.0