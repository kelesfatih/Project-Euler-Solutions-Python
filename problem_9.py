import time
import random
import math

start_time = time.time()


def spt(sum_spt):
    # a^2 + b^2 = c^2
    # a + b + c = 1000
    # a + b < 500
    # 1 < a < 250, 249 < b < 500, 499 < c < 997
    a = 2
    b = 250
    c = math.sqrt(a) + math.sqrt(b)
    while a + b + c != sum_spt:
        a = random.randint(1, 250)
        b = random.randint(249, 500)
        c = math.sqrt(a ** 2 + b ** 2)
    return a * b * c


print(math.floor(spt(1000)))

end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time:", elapsed_time, "seconds")
