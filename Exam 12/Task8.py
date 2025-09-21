"""Task 8: Largest Product of Two Numbers
Write a function max_product(nums) that returns the largest product of any two numbers in the list.
"""

def max_product(nums):
    sorted_nums = sorted(nums)

    negative = sorted_nums[0] * sorted_nums[1]
    positive = sorted_nums[-1] * sorted_nums[-2]

    if negative > positive:
        return negative
    return positive

# Test Cases:
print(max_product([1,2,3,4]) == 12)
print(max_product([-10,-20,5,3]) == 200)
print(max_product([0,2]) == 0)
