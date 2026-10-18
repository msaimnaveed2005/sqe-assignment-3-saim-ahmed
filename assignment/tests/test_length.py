"""Twenty new cases for the upstream string-length validator."""
import pytest
from validators import ValidationError
from validators.length import length

MODULE = "length"
pytestmark = pytest.mark.length


def test_length(case):
    result = length(case["value"], **case["kwargs"])
    if case["expected"] == "True":
        assert result is True
    else:
        assert isinstance(result, ValidationError)
        assert bool(result) is False
