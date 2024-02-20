def is_prime(n):
    count = 0
    i = 0
    while i <= n:
        i += 1
        if n % i == 0:
            count += 1
    if count > 2 or count <= 1:
        return False
    return True
