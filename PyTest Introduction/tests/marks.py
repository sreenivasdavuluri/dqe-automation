import pytest


@pytest.mark.skip(reason="This test is temporarily disabled.")
def test_skip_example():
    assert 1 + 1 == 2

import pytest
import sys


@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8 or higher")
def test_skipif_example():
    assert 1 + 1 == 2

import pytest


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (4, 5, 9),
])
def test_parametrize_example(a, b, expected):
    assert a + b == expected


import pytest
import time

@pytest.mark.slow
def test_old_example():
    time.sleep(5)
    assert True

@pytest.mark.integration
def test_integration_example():
    assert 1 + 1 == 2


# combined marks
@pytest.mark.slow
@pytest.mark.integration
def test_combined_marks():
    assert 1 + 1 == 2

