"""
3. Rotate an Array
Given a list arr, rotate it to the right by k steps.
Input:
A list of integers arr.
An integer k.
Output: Return the rotated array.
"""

def rotate_arr(arr, k):
    length = len(arr)
    rotated = [""] * length
    for index in range(length):
        new_pos = index + k
        value = arr[index]
        if new_pos > length:
            new_pos = (length - 1) - new_pos
        rotated[new_pos] = value
    return rotated

print(rotate_arr([1, 2, 3], 2))