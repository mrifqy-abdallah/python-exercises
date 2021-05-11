def sum_of_multiples(limit: int, multiples: list):
    if 0 in multiples:
        multiples.remove(0)
    return sum([i for i in range(limit) if any(i%j == 0 for j in multiples)])
    # Iterate i in range x, and store i if it's divisible by any value in multiple
    # Then sum all stored i at the end
