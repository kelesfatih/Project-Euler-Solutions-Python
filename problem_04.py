def largest_palindrome_product(n):
    # assign the largest multiplier with n-digit
    largest_multiplier = int(''.join("9" for i in range(n)))
    # assign the smallest multiplier with n-digit
    smallest_multiplier = largest_multiplier//9 - int(''.join("1" for i in range(n-1)))
    # assign the multiplier 1 and multiplier 2 to largest multiplier as a starting point
    multiplier_1 = multiplier_2 = largest_multiplier
    # an empty list to store palindromes
    palindromes = []
    
    # In this loop we basically subtract 1 from multiplier 2 and if it reaches smallest multiplier
    # we subtract 1 from multiplier 1 and by doing this we ensure that we check every multiplication
    # within the range of n-digit numbers.
    while smallest_multiplier <= multiplier_1:
        if str(multiplier_1 * multiplier_2) == str(multiplier_1 * multiplier_2)[::-1]:
            palindromes.append(multiplier_1 * multiplier_2)
            multiplier_2 -= 1
        if multiplier_2 <= smallest_multiplier:
            multiplier_2 = largest_multiplier
            multiplier_1 -= 1
        else:
            multiplier_2 -= 1
    return max(palindromes)


print(largest_palindrome_product(3))
