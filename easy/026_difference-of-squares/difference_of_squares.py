def square_of_sum(number:int):
    return (number * (number + 1) / 2) ** 2
    # Source: https://www.programiz.com/python-programming/examples/sum-natural-number


def sum_of_squares(number:int):
    return (number * (number + 1) / 2) * (2 * number + 1) / 3
    # Source: https://www.geeksforgeeks.org/sum-squares-first-n-natural-numbers/


def difference_of_squares(number):
    return abs(
        square_of_sum(number) - sum_of_squares(number)
    )
