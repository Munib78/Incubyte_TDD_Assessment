import eight


def test_nums_with_multiple_delimiter():
    # Test when the input string uses 2 types of delimiter
    result = eight.add("//[*][%]\n1*2%3")
    assert result == 6

def test_nums_with_string_delimiter():
    # Test when the input string uses deleminator of more than lenght 1 as delimiters
    result = eight.add("//[***]\n1***2***3")
    assert result == 6

def test_nums_with_multiples_delimiter():
    # Test when the input string uses 3 types of delimiter
    result = eight.add("//[*][%][>]\n1*2%3>4")
    assert result == 10
