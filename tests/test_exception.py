import pytest 


def divide(a, b):
    return a / b 

def test_by_non_zero():    # Test normal division
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(-6, 2) == -3

def test_divide_by_zero():
    # Ensure ZeroDivisionError is raised when dividing by zero
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
