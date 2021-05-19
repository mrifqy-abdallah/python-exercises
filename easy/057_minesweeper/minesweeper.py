from re import match


def annotate(minefield: 'list[str]') -> 'list[str]':
    len_rows = len(minefield)
    len_columns = set(map(len, minefield))

    # In case minefield is an empty list, OR,
    # In case minefield consists of empty string, like this ["", "", ""]
    #       Without this check, minefield like the one above will be considered invalid at the second `raise ValueError`
    #       In such case, we want to return the list as is, not raising exception
    if not len_rows or len_columns == {0}:  
        return minefield

    if len(len_columns) > 1:
        raise ValueError("Each row in the minefield must have the same size.")

    annotation = []
    valid = lambda x: match(r'^[ \*]+$', x)
    # len_columns is a set, and only has one int value (if it has more than one, 
    #                                                   the code must be stopped at the first `raise ValueError`)
    # What we need from len_columns from now on is the int, so we do this
    len_columns = len_columns.pop()

    for ind_row, row in enumerate(minefield):
        if not valid(row):
            raise ValueError("Invalid element detected! Valid elements are only space and asterisk.")

        annotated_row = ""
        for ind_element, element in enumerate(row):
            if element == "*":
                annotated_row += "*"
                continue
            
            # If element is a space, see its surrounding
            surrounding_element = ""
            for i in range(max(0, ind_row - 1), min(len_rows, ind_row + 2)):
                for j in range(max(0, ind_element - 1), min(len_columns, ind_element + 2)):
                    surrounding_element += minefield[i][j]

            count = surrounding_element.count("*")
            annotated_row += str(count) if count > 0 else " "
        
        annotation.append(annotated_row)
    
    return annotation