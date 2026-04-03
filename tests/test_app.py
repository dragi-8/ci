import pytest


def calculate_powers(number):
    """Helper function to calculate square, cube, and fifth power."""
    return {
        "square": number ** 2,
        "cube": number ** 3,
        "fifth_power": number ** 5
    }


def test_calculate_square():
    """Test square calculation."""
    result = calculate_powers(5)
    assert result["square"] == 25


def test_calculate_cube():
    """Test cube calculation."""
    result = calculate_powers(3)
    assert result["cube"] == 27


def test_calculate_fifth_power():
    """Test fifth power calculation."""
    result = calculate_powers(2)
    assert result["fifth_power"] == 32


def test_zero_input():
    """Test that zero input returns zeros."""
    result = calculate_powers(0)
    assert result["square"] == 0
    assert result["cube"] == 0
    assert result["fifth_power"] == 0


def test_negative_number():
    """Test negative number calculations."""
    result = calculate_powers(-2)
    assert result["square"] == 4
    assert result["cube"] == -8
    assert result["fifth_power"] == -32
