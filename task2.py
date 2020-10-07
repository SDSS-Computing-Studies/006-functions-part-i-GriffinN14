#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""
def largest(a):
    a.sort()
    g = len(a) - 1
    return a[g]
print (largest([5,1,12.3]))
