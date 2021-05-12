def square(number: int):
    if number <= 0 or number > 64:
        raise ValueError("Inserted number must be in the range of 1 to 64")
    return 2 ** (number - 1)


def total():
    return 2 ** 64 - 1
    # Source: https://en.wikipedia.org/wiki/Wheat_and_chessboard_problem#Solutions
