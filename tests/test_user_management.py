import pytest 
from app.user_management import User, is_adult


@pytest.mark.parametrize("name, age, expected", [
    ("Alice", 30, True),
    ("Bob", 17, False),
    ("Charlie", 18, True),
])
def test_is_adult(name, age, expected):
    user = User(name, age)
    assert is_adult(user) == expected

def test_is_negative_age():
    with pytest.raises(ValueError):
        User("Dave", -5)