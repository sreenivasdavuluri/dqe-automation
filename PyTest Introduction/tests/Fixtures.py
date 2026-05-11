import pytest

# Define a fixture
@pytest.fixture
def sample_data():
    return {"name": "John", "age": 30}

# Use the fixture in a test
def test_sample_data(sample_data):
    assert sample_data["name"] == "John"
    assert sample_data["age"] == 30


@pytest.fixture(scope="function")  # Default scope
def sample_data():
    return {"name": "John", "age": 30}

@pytest.fixture(scope="class")
def class_data():
    return {"shared": True}

@pytest.fixture(scope="module")
def module_data():
    return {"module": True}

@pytest.fixture(scope="package")
def package_data():
    return {"package": "shared across package"}

@pytest.fixture(scope="session")
def session_data():
    return {"session": "shared across session"}

@pytest.fixture(params=["apple", "banana", "cherry"])
def fruit(request):
    return request.param


def test_fruit(fruit):
    assert fruit in ["apple", "banana", "cherry"]


@pytest.fixture(scope="session")
def db_connection():
    print("Creating connection...")
    connection = {"db": "shared_database"} # pseudo
    yield connection
    print("Closing connection...")

def test_1(db_connection):
    assert db_connection["db"] == "shared_database"

def test_2(db_connection):
    assert db_connection["db"] == "shared_database"

@pytest.fixture
def user():
    return {"username": "john_doe"}


@pytest.fixture
def profile(user):
    return {"username": user["username"], "bio": "Software Developer"}


def test_profile(profile):
    assert profile["username"] == "john_doe"
    assert profile["bio"] == "Software Developer"

import pytest


# A fixture that returns a function
@pytest.fixture
def generate_square_function():
    def square(num):
        return num * num

    return square


# Test cases using the fixture
def test_square_positive(generate_square_function):
    square = generate_square_function
    assert square(3) == 9
    assert square(5) == 25


def test_square_negative(generate_square_function):
    square = generate_square_function
    assert square(-4) == 16
    assert square(-7) == 49





def test_square_zero(generate_square_function):
    square = generate_square_function
    assert square(0) == 0