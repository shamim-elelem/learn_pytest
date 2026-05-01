import pytest 

# 1. Custom Mark: "smoke" (Essential tests)
@pytest.mark.smoke
def test_user_can_login():
    assert True 

# 2. Custom Mark: "checkout" (feature specific)
@pytest.mark.checkout
def test_user_can_add_item_to_cart():
    assert True

# 3. Custom Mark: "api" (Interface specific)
@pytest.mark.api
@pytest.mark.slow
def test_api_response_time():
    import time 
    time.sleep(2)  # Simulate slow API response
    assert True

@pytest.mark.slow  # You can have multiple marks!
def test_external_payment_gateway():
    import time
    time.sleep(3)
    assert True
