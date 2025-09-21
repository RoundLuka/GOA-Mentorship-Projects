# 15) Count of Smaller Numbers After Self
"""
Instructions:
Given an array, for each element, count how many smaller elements are to its right.
"""

def count_smaller(arr):
    length = len(arr)
    result = []
    for index in range(length):
        count = 0
        current = arr[index]
        for index2 in range(index, length):
            if current > arr[index2]:
                count += 1
        result.append(count)
    return result


# Test Cases:
# [5, 2, 6, 1] → [2, 1, 1, 0]
#  For 5 → 2 and 1 are smaller after it
#  For 2 → 1 is smaller
#  For 6 → 1 is smaller
#  For 1 → no smaller elements
print(count_smaller([5, 2, 6, 1]))

# [1, 2, 3, 4] → [0, 0, 0, 0]
#  Increasing array, no smaller elements after any element
print(count_smaller([1, 2, 3, 4]))

# [4, 3, 2, 1] → [3, 2, 1, 0]
#  Decreasing array, every element has all smaller elements after it
print(count_smaller([4, 3, 2, 1]))

# [2, 0, 1] → [2, 0, 0]
#  2 has 0 and 1 smaller after it
#  0 and 1 have none
print(count_smaller([2, 0, 1]))

# [1] → [0]
#  Single element, no smaller elements after it
print(count_smaller([1]))