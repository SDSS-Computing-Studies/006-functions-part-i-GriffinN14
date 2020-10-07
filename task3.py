#!python3
"""
Create a function called perimeter()
The input is a list.
The return value is the sum of all the numbers in the list
added together
(2 points)
"""
def largest(a):
    a.sort()
    g = len(a) - 1
    return a[g]
print (largest([5,1,12.3]))
