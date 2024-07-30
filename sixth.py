def add(input_string) -> int:
    """
    This function takes a string with a custom delimiter and numbers,
    and returns the sum of those numbers.

    The format of the input string is assumed to be "//[delimiter]\n[numbers]".
    If the input string is empty, it returns 0.
    Raises:
        ValueError: If negative numbers are found in the input.
    """

    if input_string == "":
        return 0

    # Extract the delimiter from the input string
    delimiter = input_string[2]

    # Extract the numbers part of the input string
    numbers_string = input_string[4:]

    # Split the numbers using the delimiter
    numbers = numbers_string.split(delimiter)

    # Initialize variables
    total_sum = 0
    neg_numbers = []

    # Iterate over each number in the list of split numbers
    for number in numbers:
        num = int(number)
        if num < 0:
            neg_numbers.append(number)
        elif(num < 1000):
            total_sum += num

    if neg_numbers:
        str_neg_numbers = ', '.join(neg_numbers)
        raise ValueError(f"Negative numbers not allowed: {str_neg_numbers}")

    return total_sum
