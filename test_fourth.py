import fourth

def test_nums_with_semicolon_delimiter():
    # Test when the input string uses a semicolon as a delimiter
    result = fourth.add("//;\n1;2")
    assert result == 3

def test_nums_with_newline_delimiter():
    # Test when the input string uses newline characters as delimiters
    result = fourth.add("//\n\n4\n2\n2")
    assert result == 8

def test_nums_with_tab_delimiter():
    # Test when the input string uses tab characters as delimiters
    result = fourth.add("//\t\n1\t2\t7")
    assert result == 10
