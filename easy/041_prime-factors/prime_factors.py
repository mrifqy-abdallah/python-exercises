def factors(value: int):
    if type(value) is not int or value < 1:
        raise Exception("Please insert natural number.")
        
    factor_list = []
    i = 2

    while i * i <= value:
        while value%i == 0:
            value = value / i
            factor_list.append(i)
        i += 1
    # If last value of `value` is part of the factors
    else:
        if value > 1:
            factor_list.append(value)

    return factor_list
