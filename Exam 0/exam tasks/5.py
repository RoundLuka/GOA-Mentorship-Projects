"""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b keeping their order.

Test Cases:
a=[1,2] b=[1] -> [2]
a=[1,2,2,2,3] b=[2,3] -> [1]
a=[18, 8, -14] b=[8, -20, -16, -18] -> [18, -14]
a=[6, -9, -1] b=[-3, -4, 17, -4, 10, -16, -12, 11, -2, 17, 2, 1, 6] -> [-9, -1]
a=[-8, -2, -4, 13, 10, -12, -3, 6] b=[-3, 17] -> [-8, -2, -4, 13, 10, -12, 6]
"""

# Solution

def subtract_list(a,b):
    res = []
    for element in a:
        if element not in b:
            res.append(element)
    return res

# Test cases

print(subtract_list([1,2],[1]))
print(subtract_list([1,2,2,2,3],[2,3]))
print(subtract_list([18, 8, -14],[8, -20, -16, -18]))
print(subtract_list([6, -9, -1],[-3, -4, 17, -4, 10, -16, -12, 11, -2, 17, 2, 1, 6]))
print(subtract_list([-8, -2, -4, 13, 10, -12, -3, 6],[-3, 17]))
