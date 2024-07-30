import pytest
import fifth

def test_handle_negative_number():
    # Test if the function raises a ValueError with the correct message when a single negative number is present
    with pytest.raises(ValueError, match="Negative numbers not allowed: -2"):
        fifth.add("//\n\n4\n2\n-2")

def test_handle_multiple_negative_numbers():
    # Test if the function raises a ValueError with the correct message when multiple negative numbers are present
    with pytest.raises(ValueError, match="Negative numbers not allowed: -2, -3, -5"):
        fifth.add("//\n\n4\n2\n-2\n-3\n4\n-5")

def test_handle_without_negative_numbers():
    # Test if the function raises a ValueError with the correct message when multiple negative numbers are present
    result = fifth.add("//\n\n4\n2\n3")

    assert result == 9
