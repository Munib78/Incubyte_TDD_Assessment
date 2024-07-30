import second

def test_single_digit_nums_separated_commas():
    # Test when the input string is a comma-separated string of single-digit numbers
    result = second.add("1,2,3,4")
    assert result == 10

def test_two_or_three_digit_nums_separated_commas():
    # Test when the input string is a comma-separated string of two or three-digit numbers
    result = second.add("21,45,321")
    assert result == 387
