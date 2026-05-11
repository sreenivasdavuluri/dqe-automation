import pytest


def test_file_not_empty(csv_data):
    assert len(csv_data) > 0, "The CSV file is empty"


@pytest.mark.validate_csv
def test_validate_schema(csv_data, expected_schema):
    assert list(csv_data.columns) == expected_schema, f"Schema mismatch: expected {expected_schema}, got {list(csv_data.columns)}"


@pytest.mark.validate_csv
@pytest.mark.skip
def test_age_column_valid(csv_data):
    invalid_ages = csv_data[~csv_data['age'].between(0, 100)]
    assert len(invalid_ages) == 0, f"Invalid ages found: {invalid_ages['age'].tolist()}"


@pytest.mark.validate_csv
def test_email_column_valid(csv_data):
    email_regex = r'^[^@]+@[^@]+\.[^@]+$'
    invalid_emails = csv_data[~csv_data['email'].str.match(email_regex, na=False)]
    assert len(invalid_emails) == 0, f"Invalid email formats found: {invalid_emails['email'].tolist()}"


@pytest.mark.validate_csv
@pytest.mark.xfail
def test_duplicates(csv_data):
    duplicates = csv_data.duplicated()
    assert duplicates.sum() == 0, f"Duplicate rows found: {duplicates.sum()} duplicates"


@pytest.mark.parametrize("id, is_active", [(1, False), (2, True)])
def test_active_players(csv_data, id, is_active):
    row = csv_data[csv_data['id'] == id]
    assert not row.empty, f"No row found for id {id}"
    actual = row['is_active'].values[0]
    assert actual == is_active, f"For id {id}, expected is_active {is_active}, got {actual}"


def test_active_player(csv_data):
    row = csv_data[csv_data['id'] == 2]
    assert not row.empty, "No row found for id 2"
    assert row['is_active'].values[0] == True, "For id 2, is_active should be True"
