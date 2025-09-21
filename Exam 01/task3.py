"""3. Given an array of size n, find the majority element. The majority element is the element that appears more than n // 2 times. You may assume that the array is non-empty and the majority element always exists in the array."""

def majorElement(arr):
    majorCondition = len(arr) // 2
    for num in arr:
        if arr.count(num) > majorCondition:
            return num

# Test Cases
# [3, 2, 3] -> 3, [2, 2, 1, 1, 2] -> 2, [1, 1, 1, 1, 1] -> 1

print(majorElement([3, 2, 3])) # -> 3
print(majorElement([2, 2, 1, 1, 2])) # -> 2
print(majorElement([1, 1, 1, 1, 1])) # -> 1

