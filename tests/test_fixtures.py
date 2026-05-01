import pytest 

@pytest.fixture
def sample_data():
    """Fixture that provides sample data for testing"""
    return {"name": "Alice", "age": 30, "city": "New York"}

def test_sample_data(sample_data):
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30
    assert sample_data["city"] == "New York"