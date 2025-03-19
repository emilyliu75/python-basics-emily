from src.list_utils import count_even_numbers


def test_returns_zero_for_empty_list():
    # Arrange
    test_input = []
    expected_output = 0
    actual_output = count_even_numbers(test_input)
    assert actual_output == expected_output

