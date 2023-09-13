def prime_number(index):
    prime = 2
    counter = 0
    while index != 0:
        for i in range(2, prime + 1):
            if prime % i == 0:
                counter += 1
            if prime % i == 0 and counter == 2:
                prime += 1
                counter = 0
            if i == prime and counter == 1:
                index -= 1
                print(index)
    return prime


print(prime_number(10001))
