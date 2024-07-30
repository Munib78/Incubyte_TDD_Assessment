import first

def test_input_is_empty_string():
    result = first.add("")

    assert result == 0

def test_input_string_lenght_1():
    result = first.add("1")

    assert result == 1

def test_input_is_integer():
    result = first.add(21)

    assert result == 21


