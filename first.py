def add(input_string) -> int:
    """
    This function takes a string input and returns the sum of the numbers in the string.
    If the input string is empty, it returns 0.
    If the input string has exactly 3 characters, it returns the sum of the first two characters interpreted as integers.
    Otherwise, it returns the first character of the input string interpreted as an integer.
    """

    # If the input string is empty, return 0
    if input_string == "":
        return 0
    
    #input string has exactly 3 characters
    if len(input_string) == 3:
        # first character to an integer
        first_number = int(input_string[0])
        
        # second character to an integer
        second_number = int(input_string[2])

        # Return the sum of the first two numbers
        return first_number + second_number
    
    # If the input string has only one character return the first character as an integer
    return int(input_string[0])
