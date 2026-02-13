"""
Module providing distance calculation functions using Manhattan, Euclidean, and Minkowski metrics.
"""

def manhattan(a, b):
    """
    Calculate the Manhattan (L1) distance between two points in 2D space.

    Args:
        a (tuple): Coordinates of the first point as (x, y).
        b (tuple): Coordinates of the second point as (x, y).

    Returns:
        float: The Manhattan distance between points a and b.
    """
    return minkowski(a, b, 1)


def euclidean(a, b):
    """
    Calculate the Euclidean (L2) distance between two points in 2D space.

    Args:
        a (tuple): Coordinates of the first point as (x, y).
        b (tuple): Coordinates of the second point as (x, y).

    Returns:
        float: The Euclidean distance between points a and b.
    """
    return minkowski(a, b, 2)


def minkowski(a, b, p):
    """
    Calculate the Minkowski distance of order p between two points in 2D space.

    Args:
        a (tuple): Coordinates of the first point as (x, y).
        b (tuple): Coordinates of the second point as (x, y).
        p (int or float): Order of the Minkowski distance (p >= 1).

    Returns:
        float: The Minkowski distance of order p between points a and b.

    Raises:
        ValueError: If p is less than 1.
    """
    d_x = b[0] - a[0]
    d_y = b[1] - a[1]

    distance = (abs(d_x)**p + abs(d_y)**p)**(1/p)
    return distance
