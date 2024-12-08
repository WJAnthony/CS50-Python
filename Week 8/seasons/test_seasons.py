from seasons import user_dob
import pytest

def test_invalid_date():
    with pytest.raises(ValueError):
        user_dob("0000-10-10")
    with pytest.raises(ValueError):
        user_dob("1988-13-09")


