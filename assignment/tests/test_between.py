"""Twenty new cases for the upstream range validator."""
import pytest
from validators import ValidationError
from validators.between import between

MODULE = "between"
pytestmark = pytest.mark.between


def test_between(case):
    result = between(case["value"], **case["kwargs"])
    if case["expected"] == "True":
        assert result is True
    else:
        assert isinstance(result, ValidationError)
        assert bool(result) is False
