"""
5. Product of Array Except Self
Given an integer array nums, return an array where output[i] is the product of all elements except nums[i], without using division.
Input: A list nums (length ≥ 2).
Output: A list where each element is the product of the rest.
"""

def array_self_except(arr):
    res = []
    for index in range(len(arr)):
        product = 1
        before = arr[:index]
        after = arr[index + 1:]
        for num in before:
            product *= num
        for num in after:
            product *= num
        res.append(product)
    return res

print(array_self_except([2, 7, 9]))