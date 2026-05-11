import pytest


@pytest.fixture
def user():
    return {"username": "john_doe"}


@pytest.fixture
def profile(user):
    return {"username": user["username"], "bio": "Software Developer"}


def test_profile(profile):
    assert profile["username"] == "john_doe"
    assert profile["bio"] == "Software Developer"