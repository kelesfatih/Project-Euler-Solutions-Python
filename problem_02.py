def even_fibonacci_sum(n):
    a, b = 1, 2
    even_sum = 0

    while a <= n:
        if a % 2 == 0:
            even_sum += a
        a, b = b, a + b

    return even_sum


print(even_fibonacci_sum(4000000))
