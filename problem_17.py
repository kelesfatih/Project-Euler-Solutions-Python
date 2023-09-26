number_to_words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
}


def number_to_words_text(number):
    if number in number_to_words:
        if number == 100:
            return "onehundred"
        elif number == 1000:
            return "onethousand"
        else:
            return number_to_words[number]
    elif 21 <= number <= 99:
        tens = (number // 10) * 10
        ones = number % 10
        return f"{number_to_words[tens]}{number_to_words[ones]}"
    elif 100 <= number <= 999:
        hundreds = number // 100
        remainder = number % 100
        if remainder == 0:
            return f"{number_to_words[hundreds]}hundred"
        else:
            return f"{number_to_words[hundreds]}hundredand{number_to_words_text(remainder)}"
    elif 1000 <= number <= 9999:
        thousands = number // 1000
        remainder = number % 1000
        if remainder == 0:
            return f"{number_to_words[thousands]}thousand"
        else:
            return f"{number_to_words_text(thousands)}thousand{number_to_words_text(remainder)}"


def number_letter_counts(limit):
    counter = 0
    for i in range(1, limit + 1):
        counter += len(str(number_to_words_text(i)))
    return counter


print(number_letter_counts(1000))
