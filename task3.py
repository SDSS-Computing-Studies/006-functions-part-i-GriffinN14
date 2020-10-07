#!python3
"""
Create a function called perimeter()
The input is a list.
The return value is the sum of all the numbers in the list
added together
(2 points)
"""
def perimeter(a):
    b = 0
    for i in range(len(a)):
        b = b + a[i-1]
    return b
