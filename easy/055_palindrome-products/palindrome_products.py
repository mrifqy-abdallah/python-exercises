from itertools import combinations_with_replacement


def largest(min_factor: int, max_factor: int):
    if min_factor > max_factor:
        raise ValueError("Minimum number must be less than the max")

    return find_largest_or_smallest(min_factor, max_factor, max)


def smallest(min_factor: int, max_factor: int):
    if min_factor > max_factor:
        raise ValueError("Minimum number must be less than the max")
    
    return find_largest_or_smallest(min_factor, max_factor, min)


def find_largest_or_smallest(min: int, max: int, find):
    '''largest and smallest functions shares a similiar process, so we merge it into one here'''
    the_desired_palindrome = None
    the_factors = []
    palindrome = calculate_palindrome(min, max)

    try:
        the_desired_palindrome = find(palindrome.keys())
    except:
        pass

    if the_desired_palindrome:
        the_factors = palindrome[the_desired_palindrome]

    return the_desired_palindrome, the_factors


def calculate_palindrome(min: int, max: int):
    '''Find palindrome(s) in the given range'''
    palindromes = {}
    factors = combinations_with_replacement(range(min, max + 1), 2)
    
    for f in factors:
        multiply = f[0] * f[1]
        if str(multiply) == str(multiply)[::-1]:
            if multiply not in palindromes:
                palindromes[multiply] = []
            palindromes[multiply].append(list(f))

    return palindromes

