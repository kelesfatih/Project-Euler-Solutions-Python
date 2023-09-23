def hdtn(div):
    n = 1
    triangular_number = (n * (n + 1)) // 2
    counter = 0
    while counter < div:
        for i in range(1, int(triangular_number**0.5) + 1):
            if triangular_number % i == 0:
                counter += 2
        if triangular_number ** 0.5 == int(triangular_number ** 0.5):
            counter -= 1
        if counter < div:
            counter = 0
            n += 1
            triangular_number = (n * (n + 1)) // 2
    return triangular_number


print(hdtn(500))
