def rectangles(strings: 'list[str]') -> int:
    if not strings:
        return 0

    if len(set(map(len, strings))) > 1:
        raise ValueError("Your input is not a rectangle.")

    rows = len(strings)
    columns = len(strings[0])
    counts = 0

    for r, row in enumerate(strings):
        if "+" in row:
            for i, element in enumerate(row):
                if element == "+":
                    left = i
                    for j in range(i + 1, columns):
                        if strings[r][j] == "+":
                            right = j
                            for k in range(r + 1, rows):
                                # Ignore incomplete rectangle 
                                if strings[k][left] not in "+|" or strings[k][right] not in "+|":
                                    break

                                if strings[k][left] == "+" and strings[k][right] == "+":
                                    counts += 1

    return counts
