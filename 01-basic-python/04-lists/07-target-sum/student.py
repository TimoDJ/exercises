# 8 testen fout
# def target_sum(ns, target):
#     for i in range(len(ns)):
#         for y in range(i + 1, len(ns), 2):
#             if ns[i] + ns[y] == target or (ns[i] and ns[y]) * 2 == target:
#                 return True
#     return False

# Juist
# def target_sum(ns, target):
#     for i in range(len(ns)):
#         for y in range(0, len(ns)):
#             if ns[i] + ns[y] == target:
#                 return True
#     return False


def target_sum(ns, target):
    for x in ns:
        for y in ns:
            if x + y == target:
                return True
    return False
