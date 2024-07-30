def add(input_string) -> int:

    if(input_string == ""):
        return 0
    
    else:
        if(len(input_string) == 3):
            num1 = int(input_string[0])
            num2 = int(input_string[1])

            return num1 + num2
        
        else:
            return int(input_string[0])
