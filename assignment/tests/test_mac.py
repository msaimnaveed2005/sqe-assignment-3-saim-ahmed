"""Twenty new cases for the upstream MAC-address syntax validator."""
import pytest
from validators import ValidationError
from validators.mac_address import mac_address

MODULE = "mac"
pytestmark = pytest.mark.mac


def test_mac_address(case):
    result = mac_address(case["value"], **case["kwargs"])
    if case["expected"] == "True":
        assert result is True
    else:
        assert isinstance(result, ValidationError)
        assert bool(result) is False
