import second

def test_single_digit_nums_seperated_commas():
    result = second.add("1,2,3,4")

    assert result == 10

def test_two_or_three_digit_nums_seperated_commas():
    result = second.add("21,45,321")

    assert result == 387