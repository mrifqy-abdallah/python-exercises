class Queen:
    def __init__(self, row: int, column: int):
        _range = range(8)
        if not all((row in _range, column in _range)):
            raise ValueError("Row and column's range are 0-7")

        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        rows_is_equal = self.row == another_queen.row
        column_is_equal = self.column == another_queen.column

        # Raise exception if both queens' row and column is equal
        if rows_is_equal and column_is_equal:
            raise ValueError("Two queens cannot be placed in the same position")

        if (rows_is_equal or column_is_equal) or \
            abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True
        return False
