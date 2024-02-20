def odd_keys_dict(dictionary):
    new_dictionary = dict()

    for key, value in dictionary.items():
        if key % 2 != 0:
            new_dictionary[key] = value
    return new_dictionary
