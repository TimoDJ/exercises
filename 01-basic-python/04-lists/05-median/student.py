# def median(ns):
#     if len(ns) % 2 == 0:
#         return (ns[len(ns) // 2] + ns[(len(ns) // 2) - 1]) / 2
#     else:
#         return ns[len(ns) // 2]


# Sorteren
def median(ns):
    ns.sort()
    if len(ns) % 2 == 0:
        return (ns[len(ns) // 2] + ns[(len(ns) // 2) - 1]) / 2
    else:
        return ns[len(ns) // 2]
