def merge_dicts(dict1, dict2):
    result = dict()

    for k, v in dict1.items():
        result[k] = v

    for k2, v2 in dict2.items():
        if k2 in result:
            result[k2] = v2
        result[k2] = v2
    return result

    # of return {**dictionary1, **dictionary2}      # Deze syntax zorgt ervoor dat de dictionaries mergen,
    # als er een key voorkomt in beide zal automatisch de key van dict2 de key van dict1 overwriten


print(merge_dicts({"a": 1, "b": 2, "c": 3}, {"c": 33, "d": 44, "e": 55}))
