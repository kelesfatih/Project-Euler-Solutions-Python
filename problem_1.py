import numpy as np


def mul_3_5(number):
    numbers = np.arange(number)
    div_3_5 = numbers[(numbers % 3 == 0) | (numbers % 5 == 0)]
    result = np.sum(div_3_5)
    print(result)


mul_3_5(1000)
