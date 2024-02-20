def create_dictionary(keys, values):
    dictionary = dict()
    for i in range(len(keys)):
        for y in range(len(values)):
            if i == y:
                dictionary[keys[i]] = values[y]
    return dictionary
