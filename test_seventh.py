import seventh


def test_nums_with_semicolon_delimiter():
    # Test when the input string uses a semicolon as a delimiter
    result = seventh.add("//[;]\n1;2")
    assert result == 3

def test_nums_with_newline_delimiter():
    # Test when the input string uses newline characters as delimiters
    result = seventh.add("//[\n]\n4\n2\n2")
    assert result == 8

def test_nums_with_string_delimiter():
    # Test when the input string uses tab characters as delimiters
    result = seventh.add("//[***]\n1***2***3")
    assert result == 6
