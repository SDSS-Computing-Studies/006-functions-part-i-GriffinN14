#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
import math
def hypotenuse(a,b,c):
    if c == True:
        h = math.sqrt(a * a + b * b)
        return h
    else:
        if a > b:
            h = math.sqrt(a * a - b * b)
            return h
        elif b > a:
            h = math.sqrt(b * b - a * a)
            return h
