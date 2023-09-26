import numpy as np


def longest_collatz_seq(n):
    counter_list = np.zeros(n)
    x = n
    while n != 1:
        if n % 2 == 0:
            n //= 2
            counter_list[x - 1] += 1
        elif n % 2 != 0:
            n = 3 * n + 1
            counter_list[x - 1] += 1
        if n == 1:
            counter_list[x - 1] += 1
            n = x - 1
            x -= 1
    return np.argmax(counter_list) + 1


print(longest_collatz_seq(1000000))
