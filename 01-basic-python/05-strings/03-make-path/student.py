def make_path(parts):
    string = ""
    for part in parts:
        string += f"{part}/"
    return string[:-1]


"""
def make_path(parts):
    return "/".join(parts)
"""


print(make_path(["a", "b", "c"]))
