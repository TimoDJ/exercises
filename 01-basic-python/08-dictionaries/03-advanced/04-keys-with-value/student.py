def keys_with_value(dictionary, number):
    new_list = []
    for k, v in dictionary.items():
        if v == number:
            new_list.append(k)
    return new_list
