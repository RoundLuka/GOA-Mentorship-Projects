# 13) Maximum Product Subarray
"""
Instructions:
Find the contiguous subarray within an array which has the largest product.
"""

def max_product(arr):
    length = len(arr)
    product = arr[0] * arr[1]
    for index in range(length):
        position = index
        current = 1
        while position < length:
            current = current * arr[position]
            position += 1
        if current > product:
            product = current
    return product

# Test Cases:
# [2,3,-2,4] → 6
print(max_product([2,3,-2,4]))

# [-2,0,-1] → 0
print(max_product([-2,0,-1]))

# [0,-3,1,-2] → 1 or 6
print(max_product([0,-3,1,-2]))