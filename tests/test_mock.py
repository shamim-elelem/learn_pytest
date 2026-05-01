from unittest.mock import MagicMock


def fetch_data(api):
    return api.get_data()

def test_fetch_data():
    # Create a mock API object 
    mock_api = MagicMock()
    # Define the return value for the get_data method
    mock_api.get_data.return_value = {"value": 42}
    # Call the function with the mock API
    result = fetch_data(mock_api)
    print("Result from fetch_data:", result)
    # Assert that the result is as expected
    assert result == {"value": 42}
