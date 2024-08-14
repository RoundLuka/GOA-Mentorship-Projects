"""
Write a function with the rules:

returns true  / True if every element in an array is an integer or a float with no decimals.
returns true  / True if array is empty.
returns false / False for every other input.


Test cases:
[] -> True
[1, 2, 3, 4] -> True
[1.0, 2.0, 3.0] -> True
[1.0, 2.0, 3.0001] -> False
["-1"] -> False
"""

# Solution

def num_check(arr):
    if arr == []:
        return True
    
    for num in arr:
        if type(num) != type(1):
            if type(num) != type(1.0):
                if num != int(num):
                    return False
        if type(num) != type(1.0):
            if type(num) != type(1):
                if num != int(num):
                    return False
    return True

# Test cases

print(num_check([]))
print(num_check([1, 2, 3, 4]))
print(num_check([1.0, 2.0, 3.0]))
print(num_check([1.0, 2.0, 3.0001]))
print(num_check(["-1"]))
