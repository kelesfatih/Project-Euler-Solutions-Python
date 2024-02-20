def largest_prime_factor(number):
    factor = 2
    while factor * factor <= number:
        if number % factor == 0:
            number //= factor
        else:
            factor += 1
    return number


print(largest_prime_factor(600851475143))
