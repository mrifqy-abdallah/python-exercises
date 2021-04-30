def is_valid(isbn):
    '''Verify ISBN-10 only'''
    isbn = isbn.replace("-", "")
    # If the ISBN is more than 10 digits, then it must be invalid
    if len(isbn) != 10:
        return False
    
    # Initiating list of number of range 10 to 1
    multiplier = [i+1 for i in reversed(range(0, 10))]
    isbn_value = 0
    
    for index, digit in enumerate(isbn):
        if digit.isdigit():
            isbn_value += int(digit) * multiplier[index]
        else:
            if digit != "X" or digit != "x":
                return False
            isbn_value += 10

    # Return true if ISBN value is divisible by 11
    return isbn_value % 11 == 0
