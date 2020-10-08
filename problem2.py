#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math
def distance(a,b):
    if a[0] > b [0]:
        c = a[0] - b [0]
    else:
        c = b[0] - a[0]
    if a[1] > b[1]:
        d = a[1] - b[1]
    else:
        d = b[1] - a[1]
    e = (c,d)
    return (e)
