"""Task 7: Subset Sum Check
Write a function has_subset_sum(nums, target) that returns True if any subset of numbers adds up to target.
"""

def has_subset_sum(nums, target):

    sum_results = {0}

    for num in nums:
        subset = set()
        for i in sum_results:
            subset.add(i)
            subset.add(i + num)
        sum_results = subset
    
    for sum_res in sum_results:
        if sum_res == target:
            return True
    return False



# Test Cases:
print(has_subset_sum([3,34,4,12,5,2], 9) == True)  # 4+5
print(has_subset_sum([3,34,4,12,5,2], 30) == False)
print(has_subset_sum([], 0) == True)