def smallest_multiple(n):
    # 20 = 4*5 18 = 9*2, 15 = 5*3, 14 = 7*2
    lst = [20, 19, 18, 17, 15, 14, 13, 11]
    for i in lst:
        if n % i != 0:
            n *= i
        elif n % i == 0:
            pass
    return n


print(smallest_multiple(20))
