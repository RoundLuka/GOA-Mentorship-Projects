"""
1. Find the Majority Element
Given a list of N integers, find the majority element (the element that appears more than N/2 times). If there is no majority element, return None.
Input: A list of integers arr.
Output: Return the majority element or None.
"""

def find_majority(arr):
    n = len(arr)
    for number in arr:
        if arr.count(number) > (n / 2):
            return number
    return None
    
print(find_majority([2, 3, 1, 1, 1, 7, 8, 1, 1, 1, 1, 9]))