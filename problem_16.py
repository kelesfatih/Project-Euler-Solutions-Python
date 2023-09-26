def power_digit_sum(base, power):
    number = base ** power
    digit_sum = 0
    for i in str(number):
        digit_sum += int(i)
    return digit_sum


print(power_digit_sum(2, 1000))
