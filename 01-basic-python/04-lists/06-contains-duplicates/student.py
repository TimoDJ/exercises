def contains_duplicates(xs):
    for i in range(len(xs)):
        for y in range(i + 1, len(xs)):
            if xs[i] == xs[y]:
                return True
    return False
