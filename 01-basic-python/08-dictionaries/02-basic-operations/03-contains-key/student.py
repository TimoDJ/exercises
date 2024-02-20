# 3 test failed  ??
# def contains_key(dictionary, key):
#     keys_list = dictionary.keys()

#     for i in keys_list:
#         if i == key:
#             return True
#     return False


def contains_key(dictionary, key):
    return key in dictionary


print(contains_key({"a": 2, "b": 5, "c": 3}, 6))
