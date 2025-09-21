"""8. Find the Kth Smallest Element in an Array

Task:
Write a function that finds the k-th smallest element in an unsorted
array.
"""

def smallestTarget(arr, k):
    # sorting array in ascending order, so smallest kth element would be element on (k - 1) index
    arr = sorted(arr)
    return arr[k - 1]
    


# Test Cases:
# ● Input: arr = [3, 2, 1, 5, 6, 4], k = 2
# Output: 2
# Explanation: The 2nd smallest element in the array is 2.
print(smallestTarget([3, 2, 1, 5, 6, 4], 2))
# ● Input: arr = [3, 2, 1, 5, 6, 4], k = 4
# Output: 4
# Explanation: The 4th smallest element in the array is 4.
print(smallestTarget([3, 2, 1, 5, 6, 4], 4))
# ● Input: arr = [7, 10, 4, 3, 20, 15], k = 3
# Output: 7
# Explanation: The 3rd smallest element in the array is 7.
print(smallestTarget([7, 10, 4, 3, 20, 15], 3))
# ● Input: arr = [1, 2, 3, 4, 5], k = 1
# Output: 1
# Explanation: The 1st smallest element is 1.
print(smallestTarget([1, 2, 3, 4, 5], 1))
# ● Input: arr = [1, 2, 3, 4, 5], k = 5
# Output: 5
# Explanation: The 5th smallest element is 5.
print(smallestTarget([1, 2, 3, 4, 5], 5))