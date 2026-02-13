
def manhattan(a,b):
    d_x = b[0] - a[0]
    d_y = b[1] - a[1]
    distance = abs(d_x) + abs(d_y)
    return distance
