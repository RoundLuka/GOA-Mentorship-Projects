"""6. Given two sorted arrays nums1 and nums2, return the mean of the two sorted arrays."""

def mean(arr1, arr2):
    combined = arr1 + arr2
    length = 0
    sum = 0
    for num in combined:
        length += 1
        sum += num
    return sum / length

# Test Cases
# [1, 2, 3], [4, 5, 6] -> 3.5,    [10, 20], [30, 40, 50] -> 30.0,    [-5, -3, -1], [1, 3, 5] -> 0.0