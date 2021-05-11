def primes(limit: int):
    prime = []
    not_prime = []
    if limit < 0:
        raise Exception("Limit value cannot be negative")

    for i in range(2, limit + 1):
        # Break if all numbers within the range has been listed
        if range(2, limit + 1) == len(prime) + len(not_prime):
            break

        if i not in not_prime:
            prime.append(i)
            # Multiples of a prime number is not a prime
            for j in range(i*i, limit + 1, i):
                not_prime.append(j)

    return prime