import pytest

class TestMathOperations:
    @pytest.mark.parametrize("a, b, expected", [(5, 10, 15), (2, 3, 5)])
    def test_add(self, a, b, expected):
        assert a + b == expected

    @pytest.mark.parametrize("a, b, expected", [(10, 5, 5), (5, 2, 3)])
    def test_subtract(self, a, b, expected):
        assert a - b == expected