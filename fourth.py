def add(input_string) -> int:
    """
    This function takes a string with a custom delimiter and numbers, 
    and returns the sum of those numbers.
    
    The format of the input string is assumed to be "//[delimiter]\n[numbers]".
    If the input string is empty, it returns 0.
    """

    if input_string == "":
        return 0

    # Extract the delimiter from the input string
    delimiter = input_string[2]

    # Extract the numbers part of the input string
    numbers_string = input_string[4:]

    # Split the numbers using the delimiter
    numbers = numbers_string.split(delimiter)
    
    #store the sum of the numbers
    total_sum = 0

    # Iterate over each number in the list of split numbers
    for number in numbers:
        total_sum += int(number)

    #sum of all numbers
    return total_sum
