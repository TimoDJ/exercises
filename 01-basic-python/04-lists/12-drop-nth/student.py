def drop_nth(xs, n):
    new_list = []
    for element in range(len(xs)):
        if element != n:
            new_list.append(xs[element])
    return new_list
