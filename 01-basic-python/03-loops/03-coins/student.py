def coins(one, two, five, goal):
    one = one * 1
    two = two * 2
    five = five * 5

    sum = one + two + five
    print(sum)
    if goal % sum == 0:
        return True
    return False


print(coins(2, 1, 1, 8))
