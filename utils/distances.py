import math

def manhattan(a,b):
    d_x = b[0] - a[0]
    d_y = b[1] - a[1]
    distance = abs(d_x) + abs(d_y)
    return distance


def euclidean(a, b):
    d_x = b[0] - a[0]
    d_y = b[1] - a[1]

    distance = (d_x**2) + (d_y**2)
    return math.sqrt(distance)
