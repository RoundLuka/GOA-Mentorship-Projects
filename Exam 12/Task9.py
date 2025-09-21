"""Task 9: Longest Increasing Subsequence Length
Write a function lis_length(nums) that returns the length of the longest strictly increasing subsequence.
"""

def lis_length(nums):
    length = len(nums)
    longest = 0
    for i in range(length):
        number = nums[i]
        current = 1
        compare = number
        for j in range(i, length):
            if compare < nums[j]:
                current += 1
                compare = nums[j]
        if current > longest:
            longest = current
    return longest


# Test Cases:
print(lis_length([10,9,2,5,3,7,101,18]) == 4)  # [2,3,7,101]
print(lis_length([0,1,0,3,2,3]) == 4)
print(lis_length([7,7,7,7]) == 1)