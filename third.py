def add(input_string):

    numbers_with_newline = input_string.split(",")

    #list to store numbers after removing delimiters
    numbers = []

    for item in numbers_with_newline:
        #if the element contains a newline character
        if "\n" in item:
            # Split the element by newline character to handle newline-separated numbers
            split_numbers = item.split("\n")
            
            # Add each split number to the numbers list
            for number in split_numbers:
                numbers.append(int(number))
        else:
            # Add the number directly to the numbers list after converting to integer
            numbers.append(int(item))
    

    return sum(numbers)