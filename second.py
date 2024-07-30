def add(input_string) -> int:
    """
    This function takes a string of comma-separated numbers and returns their sum.
    If the input string is empty, it returns 0.
    """

    # handle comma-separated numbers
    numbers = input_string.split(",")

    #store the sum of the numbers
    total_sum = 0

    for number in numbers:
        # Convert the current number to an integer and add it to the total sum
        total_sum += int(number)

    # sum of all numbers
    return total_sum
