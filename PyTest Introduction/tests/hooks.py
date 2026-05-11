import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="dev", help="Environment to run tests against"
    )


@pytest.fixture
def env(request):
    return request.config.getoption("--env")


def pytest_collection_modifyitems(config, items):
    for item in items:
        if "slow" in item.name:
            item.add_marker(pytest.mark.slow)