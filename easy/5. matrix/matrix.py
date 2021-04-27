class Matrix:
    def __init__(self, matrix_string):
        '''Normalize the matrix_string into a proper list'''
        
        rows = matrix_string.split("\n")
        normalized_list = []
        for row in rows:
            elements = row.split()  # resulted split are in str, like ["1", "2", "3"]
            map_numbers = map(int, elements)  # map the value int the list to int all at once
            list_int = list(map_numbers)  # turn the map into list
            normalized_list.append(list_int)
        self.matrix = normalized_list
        
        # The one-line version
        # Same output, but the process is slightly different (the one-line version use nested loops instead of map)
        '''
        self.matrix = [[int(elements) for elements in rows.split()] for rows in matrix_string.split("\n")]
        '''

    def row(self, index):
        '''Return the row at the given index'''
        return self.matrix[index - 1]

    def column(self, index):
        '''Return the column at the given index'''
        return [row[index - 1] for row in self.matrix]
        