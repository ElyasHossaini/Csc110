import doctest
import math


'''
Q1. This is a function I left you to complete in a previous lecture
Update this function so it returns the length of the adjacent side.
Design a second function that will return the length of the opposite side.
'''


def print_adjacent_length(hypotenuse: float, angle: float) -> float:
    """ calculates and prints the length of the side of a right-angle
    triangle adjacent to given angle in degrees and given hypotenuse length
    Precondition: hypotenuse and angle > 0
    >>> print_adjacent_length(13.2, 60)
    6.6
    >>> print_adjacent_length(28.7, 29.8)
    24.9
    """
    radians = math.radians(angle)  # using built-in radians function
    adjacent = math.cos(radians) * hypotenuse
    return adjacent

def print_opposite_length(hypotenuse: float, angle: float) -> float:
    """ calculates and prints the length of the side of a right-angle
    triangle adjacent to given angle in degrees and given hypotenuse length
    Precondition: hypotenuse and angle > 0
    >>> print_adjacent_length(13.2, 60)
    6.6
    >>> print_adjacent_length(28.7, 29.8)
    24.9
    """
    radians = math.radians(angle)  # using built-in radians function
    opposite = math.sin(radians) * hypotenuse
    return opposite
'''
Q2. Design a new function that takes the length the hypotenuse of a triangle
and the angle (in degrees) of one of the non-right angles,
and calculates and returns the perimeter of the triangle.
'''
def perimeter(hypotenuse: float, angle: float) -> float:
    opposite = print_opposite_length(hypotenuse, angle)
    adjacent = print_adjacent_length(hypotenuse, angle)
    perimeter = opposite + adjacent + hypotenuse
    return perimeter

'''
Q3. Design a new function that takes the length of the hypotenuse of a triangle
and the angle in degrees of one of the non-right angles, and prints the
name of the longest side other than the hypotenuse.

The function should print:
-adjacent if the side adjacent to the given angle
 is the longest side after the hypotenuse
-opposite if the side opposite to the given angle
 is the longest side after the hypotenuse
-equal if the adjacent and opposite sides to the given angle
 are less than 0.01 different from each other
'''
def longest_side(hypotenuse: float, angle: float) -> None:
    opposite = print_opposite_length(hypotenuse, angle)
    adjacent = print_adjacent_length(hypotenuse, angle)
    
    if opposite == adjacent:
        print('equal')
    elif adjacent > opposite:
        print('adjacent')
    else:
        print('opposite')
        

'''
Q4. Design a function that takes two strings and returns the
result of those two strings joined together.
'''
def strings_attached(word1: str, word2: str) -> str:
    return word1 + word2