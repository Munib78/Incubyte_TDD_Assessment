def add(input_string: str) -> int:
    """
    This function processes a string that specifies a custom delimiter and a list of numbers,
    and returns the sum of those numbers.

    The input string format is expected to be "//[delimiter]\n[numbers]".
    If the input string is empty, the function returns 0.
    If any negative numbers are present in the input, a ValueError is raised with a message 
    listing all negative numbers.

    Parameters:
        input_string (str): The input string containing the delimiter and numbers.

    Returns:
        int: The sum of the numbers in the input string.

    Raises:
        ValueError: If negative numbers are found in the input string.
    """

    # Return 0 for an empty input string
    if input_string == "":
        return 0

    # Extract the delimiter from the input string
    delimiter = ""
    delimiter_end_index = 0

    # Find the end of the delimiter section
    for idx in range(3, len(input_string)):
        if input_string[idx] == ']':
            delimiter_end_index = idx
            break
        else:
            delimiter += input_string[idx]

    # Extract the portion of the input string containing numbers
    numbers_section = input_string[delimiter_end_index + 2:]

    # Split the numbers using the extracted delimiter
    number_strings = numbers_section.split(delimiter)

    # Initialize sum and list for negative numbers
    total_sum = 0
    negative_numbers = []

    # Process each number in the split list
    for number_string in number_strings:
        if number_string:  # Ignore empty strings
            number = int(number_string)
            if number < 0:
                negative_numbers.append(number_string)
            elif number < 1000:
                total_sum += number

    # Raise an error if there are negative numbers
    if negative_numbers:
        negative_numbers_str = ', '.join(negative_numbers)
        raise ValueError(f"Negative numbers not allowed: {negative_numbers_str}")

    return total_sum
