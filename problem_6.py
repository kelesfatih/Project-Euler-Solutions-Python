import numpy as np


def ssq(n):
    sum_of_squares = sum(np.arange(1, n + 1) ** 2)
    square_of_sum = sum(np.arange(1, n + 1)) ** 2
    return square_of_sum - sum_of_squares


print(ssq(100))
