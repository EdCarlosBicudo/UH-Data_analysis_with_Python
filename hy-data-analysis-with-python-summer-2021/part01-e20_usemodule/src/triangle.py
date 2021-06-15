import math

__doc__ = """Module to calculate the hypothenuse and the area of a given triangle
"""


def hypothenuse(s1, s2):
    """Returns the length of the hypothenuse when given the lengths of two \
other sides of a right-angled triangle

    Args:
        s1 (float): Side 1
        s2 (floar): Side 2

    Returns:
        float: hypothenuse
    """
    return math.sqrt(s1 ** 2 + s2 ** 2)

def area(s1, s2):
    """returns the area of the right-angled triangle, when two sides, \
perpendicular to each other, are given as parameters.

    Args:
        s1 (float): Side 1
        s2 (float): Side 2

    Returns:
        float: area
    """
    return (s1 * s2) / 2

__version__ = "1.0"

__author__ = "Ed Carlos Bicudo"