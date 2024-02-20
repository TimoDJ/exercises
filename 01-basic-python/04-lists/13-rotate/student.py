# Dit werkt ook ??
"""
def rotate(xs, n):
    for i in range(len(xs)):
        if i == n:
            end = xs[i:]
            beginning = xs[:i]
    return end + beginning
"""


def rotate(xs, n):
    for _ in range(n):
        x = xs.pop(0)
        xs.append(x)
