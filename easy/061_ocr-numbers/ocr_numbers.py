OCR_DICT = {
    " _ | ||_|": "0",
    "     |  |": "1",
    " _  _||_ ": "2",
    " _  _| _|": "3",
    "   |_|  |": "4",
    " _ |_  _|": "5",
    " _ |_ |_|": "6",
    " _   |  |": "7",
    " _ |_||_|": "8",
    " _ |_| _|": "9",
    ",": ","
}

def convert(input_grid: 'list[str]') -> str:
    row_size_is_valid = len(input_grid) % 4 == 0
    column_size_is_valid = all(map(lambda x: len(x) % 3 == 0, input_grid))

    if not row_size_is_valid or not column_size_is_valid:
        raise ValueError("Grid's row must be in the multiple of 3, and the column must be in the multiple of 4")
    
    parse_per_number = []
    
    # Iterate through input_grid for each 4 rows
    for i in range(0, len(input_grid), 4):
        # Parse the number. Each number is written in 3 columns...
        for j in range(0, len(input_grid[0]), 3):
            number = []
            # ...and 3 rows
            # The fourth row is just spaces, so there's no need to check it
            for k in range(3):
                number.append(input_grid[i+k][j:j+3])
                
            parse_per_number.append("".join(number))

        # Numbers in each 4 rows is separated by comma...
        parse_per_number.append(",")

    # ...But the last comma in the list is not necessary
    parse_per_number.pop()

    result = [OCR_DICT[i] if i in OCR_DICT else "?" for i in parse_per_number]
    return "".join(result)