"""1. Given an array containing n-1 numbers taken from the range 1 to n, write a function to find the missing number. There are no duplicates in the array."""

def findMissing(arr):
    arr_sum = 0
    length = 0
    for num in arr:
        length += 1
        arr_sum += 1


    sum = 0
    start = arr[0]
    end = start + length
    for i in range(start, end):
        sum += i
    return sum - arr_sum

# Test Cases
#[1, 2, 4, 5] -> 3, [1] -> 2, [2, 3, 1, 5] -> 4

print(findMissing([1, 2, 4, 5])) # -> 3
print(findMissing([1])) # -> 1
print(findMissing([2, 3, 1, 5])) # ->  4

