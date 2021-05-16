from math import sqrt


def prime(number: int):
    if number <= 0:
        raise ValueError("Inserted value cannot be less than zero.")
    return nth_prime(number)


def nth_prime(n: int):
    prime_list = [2]
    check_this_number = 3

    while len(prime_list) < n:
        limit = sqrt(check_this_number)
        is_prime = True
        for i in prime_list:
            # We just need to check check_this_number againts prime numbers up to its square root
            # Source: https://stackoverflow.com/a/5811176/12725825
            if i > limit:
                break
            if check_this_number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(check_this_number)
        
        # Even numbers doesnt need to be checked
        check_this_number += 2

    # Picking only the last (nth) prime
    return prime_list[-1]
    