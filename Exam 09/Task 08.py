# 8) Rotate List by K Positions
"""
Instructions:
Write a function that rotates a list to the right by k positions.
"""

def rotate(arr, k):
    length = len(arr)
    new_arr = ["|||"] * length
    for index in range(length):
        try:
            new_arr[index + k] = arr[index]
        except:
            new_arr[(index + k) - length] = arr[index]
    return new_arr
# Test Cases:
# [1,2,3,4,5], 2 → [4,5,1,2,3]
print(rotate([1,2,3,4,5], 2))

# [1,2,3], 1 → [3,1,2]
print(rotate([1,2,3], 1))

# [1], 0 → [1]
print(rotate([1], 0))

# [], 3 → []
print(rotate([], 3))

# [1,2,3,4], 4 → [1,2,3,4]
print(rotate([1,2,3,4], 4))