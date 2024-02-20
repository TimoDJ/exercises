def last_digit(digit):
    count = 0
    while count < len(str(digit)):
        count += 1
        return digit % 10**count


def remove_last_digit(digit):
    count = 0
    while count < len(str(digit)):
        count += 1
        return digit // 10**count


def digit_sum(digit):
    first_digit = str(digit)[0]
    sum = int(first_digit)
    while len(str(digit)) != 1:
        sum += last_digit(digit)
        digit = remove_last_digit(digit)
    return sum
