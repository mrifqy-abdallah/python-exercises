from math import ceil

def classify(number: int):
    if type(number) is not int or number < 1:
        raise ValueError("Please insert natural number.")

    if number == 1:
        return "deficient"
        
    limit = ceil(number / 2)
    factors = filter(lambda x: number % x == 0, range(1, limit+1))

    return determine(number, sum(factors))

def determine(number: int, sum_of_factors: int):
    if sum_of_factors > number:
        return "abundant"
    elif sum_of_factors < number:
        return "deficient"
    return "perfect"