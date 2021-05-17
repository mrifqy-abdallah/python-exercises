def saddle_points(matrix: list):
    saddle = []

    if len(set(map(len, matrix))) > 1:
        raise ValueError("Matrix is irregular! Each row must be in the same size.")

    if matrix:
        # Transpose matrix to access it by columns
        transpose_matrix = list(zip(*matrix))

        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                if value == max(row) == min(transpose_matrix[j]):
                    saddle.append({"row": i + 1, "column": j + 1})

    return saddle
    