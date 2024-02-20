# Fout
# def includes(xs, ys):
#     for i in range(len(xs)):
#         for y in range(len(ys)):
#             if xs[i] != ys[y]:
#                 return False
#     return True


def includes(xs, ys):
    for y in ys:
        if y not in xs:
            return False
    return True
