import math


def tri(a, b, c):
    s = (a + b + c)/2
    result = math.sqrt(s*(s - a)*(s - b)*(s- c))
    return float(result)


print(tri(3, 4, 5))
