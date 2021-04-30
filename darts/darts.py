import math
from math import sqrt


def score(x, y):
    a = sqrt(x**2 + y**2)

    if a <= 1:
        return 10
    elif a <= 5:
        return 5
    elif a <= 10:
        return 1
    else:
        return 0
