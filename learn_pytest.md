**What is Pytest?**
Pytest is a testing framework for Python.
- It lets you write small tests and scale them to complex functional tests.
- Solves the problem of manually checking your code. If your code changes, tests tell you immediately if something broke.

```bash
# install package
pip install pytest
# check version
pytest --version
```

**Naming Convention**
Python has naming convention for pytest to discover tests:
- Test files start with test_ or end with _test.py
- Test functions start with test_.

```python
# test_math.py

def add(a, b):
    """Simple addition function"""
    return a + b

def test_add():
    """Test if addition works correctly"""
    assert add(2, 3) == 5  # assert checks if result is correct
    assert add(-1, 1) == 0
```

or you can name test_math.py as math_test.py. So, when you will run
the test as 
```bash
pytest tests/
```
then Pytest automatically discovers test_*.py files and runs test_* functions.
Problem solved: Automates verification instead of manual checking.
So, problem solved! Automates verification instead of manual checking.

**Using Fixtures**
Problem: Often we need to set-up some data or resources before testing. Doing it in every test is repetitive.
Solution: `@pytest.fixture`
```python
# test_fixture.py
import pytest

# Fixture provides reusable setup
@pytest.fixture
def sample_data():
    return {"name": "Alice", "age": 25}

def test_name(sample_data):
    assert sample_data["name"] == "Alice"

def test_age(sample_data):
    assert sample_data["age"] > 20
```
Explanation:
- @pytest.fixture marks a function as a fixture.
- Tests receive fixture values as function arguments.
- Solves repetitive setup and keeps tests clean.

**Parameterized Tests**
Problem: Testing the same function with multiple inputs is tedious.
Solution: `@pytest.mark.parametrize`
```python
# test_parametrize.py
import pytest

def multiply(a, b):
    return a * b

# Run the same test with multiple values
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (0, 5, 0),
    (-1, 5, -5)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected
```
Explanation:

- Each tuple is a set of inputs + expected result.
- Pytest runs the function for each tuple.
- Solves problem of duplicating similar test code.

**Testing for Exceptions**
Problem: Functions may raise exceptions. We need to ensure they do so when expected.
```python
# test_exception.py
import pytest

def divide(a, b):
    return a / b

def test_divide_by_zero():
    # Ensure ZeroDivisionError is raised
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
```
Explanation:
- `pytest.raises` verifies an exception is raised.
- Solves problem of silently failing or unexpected crashes.

**Grouping Tests with Classes**
- Useful for organizing related tests.
- Class names must start with `Test`
```python
# test_class.py

class TestMathOperations:

    def test_add(self):
        assert 2 + 3 == 5

    def test_subtract(self):
        assert 5 - 3 == 2
```
Problem solved: Better organization and readability for large projects.

**Using Setup & Teardown**
Problem: Sometimes you need to prepare and clean resources like files or databases.
```python
# test_setup_teardown.py

import pytest

@pytest.fixture
def setup_teardown():
    # Setup code
    data = {"temp_file": "example.txt"}
    yield data  # test runs here
    # Teardown code
    print(f"Cleaning up {data['temp_file']}")
```
Explanation:
- yield allows code before yield to run as setup, code after as teardown.
- Solves resource management and avoids side effects between tests.

**Mocking External Dependencies**
Problem: External APIs or databases may be slow/unreliable for tests.
Solution: Use `unittest.mock` to simulate them.
```python
# test_mock.py
from unittest.mock import MagicMock

def fetch_data(api):
    return api.get_data()

def test_fetch_data():
    mock_api = MagicMock()
    mock_api.get_data.return_value = {"value": 42}
    
    result = fetch_data(mock_api)
    assert result["value"] == 42
```
Explanation:
- Mocks simulate external dependencies.
- Solves slow/unreliable external calls in tests.

**Advanced Features**
- 9a. Marking Tests
    - Group tests using `@pytest.mark` (e.g. slow, smoke).
    ```python
        import pytest

        @pytest.mark.slow
        def test_large_computation():
            import time
            time.sleep(2)
            assert True
    ```
    - Run: `pytest -m slow`

- 9b. Running Tests in Parallel
  ```python
  pip install pytest-xdist
  pytest -n 4  # run tests on 4 cores
  ```
- 9c. Generating HTML Reports
  ```python
  pip install pytest-html
  pytest --html=report.html
  ```

**`pytest-cov`Visibility**
Problem: You wrote 50 tests, but you have no idea if you actually tested that one tricky `if/else` block in your `auth.py`.
Solution: It generates a Coverage Report. It tracks which lines of your code were executed during the tests and which were skipped.
```python
pip install pytest-cov

# use
pytest --cov=geo_utils tests_folder
```
```python
==== tests coverage ====
coverage: platform darwin, python 3.13.12-final-0

Name                              Stmts   Miss  Cover
-----------------------------------------------------
geo_utils/__init__.py                 0      0   100%
geo_utils/_utils.py                  11      8    27%
geo_utils/auth.py                    63      2    97%
geo_utils/browser_fastapi.py         12     12     0%
geo_utils/db.py                      46     46     0%
geo_utils/elasticsearch.py           58     58     0%
geo_utils/gcp/__init__.py             0      0   100%
geo_utils/gcp/pub_sub.py             21     21     0%
geo_utils/gcp/secret_manager.py      38     38     0%
geo_utils/gcp/storage.py             25     25     0%
geo_utils/gcp/vertex_ai.py           29     29     0%
geo_utils/redis.py                   84     84     0%
-----------------------------------------------------
TOTAL                               387    323    17%
====== 14 passed, 3 warnings in 2.32s =====
```
Why use it?
- It identifies "dead code" (code that is never run).
- It gives you confidence that your critical logic is actually being exercised.
- It can fail your CI/CD build if coverage drops below a certain percentage (e.g., 80%).

**`factory_boy`Efficiency & Maintenance**
Problem: In your previous example, you manually created a dictionary for the user: {"username": "admin", "role": "super-admin"}. If you add a password_hash field to your User model later, you have to go back and fix every single test that uses a user dictionary.

The Solution: You define a "Factory" once. It acts as a blueprint for generating test data.
```python
pip install factory_boy
```
```python
import factory
from my_models import User

class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user_{n}")
    role = "user"  # Default value
    email = factory.LazyAttribute(lambda o: f"{o.username}@example.com")

# In your test:
def test_admin_logic():
    # Overriding just the part we care about
    admin = UserFactory(role="super-admin") 
    assert admin.role == "super-admin"
    assert "user_" in admin.username # Automatically generated!
```
Extra:
- Faker integration comes automatically (good for generating emails, names, etc.)
- Can be used later when your DB objects get bigger.
```python
import factory
from my_app.models import User  # Your actual User model

class UserFactory(factory.Factory):
    class Meta:
        model = User

    # Basic Faker integration
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    
    # Complex Faker: Generating an email based on the names above
    email = factory.Faker("ascii_safe_email")
    
    # Generating a realistic username
    username = factory.Faker("user_name")
    
    # Setting a default role (not faked)
    role = "user"
    
    # Generating a random past date for "joined_at"
    joined_at = factory.Faker("date_time_this_year")
```
Uses:
```python
def test_user_profile_display():
    # Create a single "random" user
    user = UserFactory() 
    print(user.email) # Result: something like 'sarah_jones@example.net'
    
    # Create a specific Super Admin
    admin = UserFactory(role="super-admin", username="boss_man")
    
    assert admin.role == "super-admin"
    assert admin.username == "boss_man"
    # Even though we specified the username, Faker still filled in 
    # the first_name, last_name, and email automatically!
```

**`freezegun`Stability**
The Problem: Testing JWT expiration is a nightmare because time is always moving. If you test that a token expires in 30 minutes, you can't exactly make the test wait 30 minutes to see if it fails.

The Solution: It "freezes" the system clock at a specific moment. You can then "move" time forward manually within the test.

Why use it?
- No more time.sleep() in tests.
- Tests are deterministic (they yield the same result every time, regardless of when you run them).

```python
from freezegun import freeze_time
from auth import AuthHandler
from datetime import timedelta

@freeze_time("2026-03-28 12:00:00")
def test_jwt_expiration_with_freeze():
    # 1. Generate token at 12:00:00
    token = AuthHandler.encode_token("user123")
    
    # 2. Move time forward 31 minutes
    with freeze_time("2026-03-28 12:31:00"):
        # 3. Now the token is officially expired!
        with pytest.raises(HTTPException):
            AuthHandler.decode_token(token)
```