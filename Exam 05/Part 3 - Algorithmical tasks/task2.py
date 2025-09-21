"""
2. First Missing Positive Integer
Given a list of N integers, find the smallest missing positive integer.
Input: A list of integers arr.
Output: Return the first missing positive integer.
"""

def find_missing(arr):

    for number in range(1, len(arr)):
        if number not in arr:
            return number
        
    
print(find_missing([1, 2, 3, 5, 6]))
print(find_missing([1, 7, 4, 5, 6]))
print(find_missing([9, 7, 4, 8, 6]))