import pytest
import pandas as pd

# Fixture for path to CSV file
@pytest.fixture(scope="session")
def path_to_file():
    import os
    return os.path.join(os.path.dirname(__file__), "..", "src", "data", "data.csv")

# Fixture to read the CSV file and return its content
@pytest.fixture(scope="session")
def csv_data(path_to_file):
    df = pd.read_csv(path_to_file)
    return df

# Fixture to validate the schema of the file
@pytest.fixture(scope="session")
def validate_schema():
    def _validate(actual_schema, expected_schema):
        assert actual_schema == expected_schema, f"Schema mismatch: expected {expected_schema}, got {actual_schema}"
    return _validate

# Fixture for expected schema
@pytest.fixture(scope="session")
def expected_schema():
    return ["id", "name", "age", "email", "is_active"]


# Pytest hook to mark unmarked tests with a custom mark
def pytest_collection_modifyitems(config, items):
    for item in items:
        if not item.own_markers:
            item.add_marker(pytest.mark.unmarked)
