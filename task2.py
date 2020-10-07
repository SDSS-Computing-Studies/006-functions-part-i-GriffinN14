#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""
def largest(a,b,c,d,e,f):
    list = [a,b,c,d,e,f]
    list.sort()
    g = len(list) - 1
    return list[g]
