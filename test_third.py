import third

def test_single_digit_nums_separated_commas():
    # Test when the input string is a comma-separated string of single-digit numbers
    result = third.add("1,2,3,4")
    assert result == 10

def test_two_or_three_digit_nums_separated_commas_and_newlines():
    # Test when the input string contains a combination of commas and newlines
    result = third.add("2\n1,45,3\n21")
    assert result == 72

def test_mixed_delimiters():
    # Test when the input string contains mixed delimiters (commas and newlines)
    result = third.add("1\n2,3\n4")
    assert result == 10

