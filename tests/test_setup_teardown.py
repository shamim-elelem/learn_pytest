import pytest 


@pytest.fixture
def setup_teardown():
    # setup code 
    data = {"temp_file": "example.txt"}
    yield data 
    # teardown code
    print(f"Clearning (teardown) up resources: {data['temp_file']}")

def test_example(setup_teardown):
    # test code using setup_teardown fixture
    assert setup_teardown["temp_file"] == "example.txt"