# 14) Maximum XOR of Two Numbers in an Array
"""
Instructions:
Find two numbers in an array that yield the maximum XOR value.
"""

def max_xor(arr):
    length = len(arr)
    most = 0
    for i in range(length):
        for j in range(length):
            if i != j:
                current = arr[i] ^ arr[j]
                if current > most:
                    most = current
    return most


# Test Cases:
# [3, 10, 5, 25, 2, 8] → 28
#  Max XOR between 5 and 25: 5 ^ 25 = 28
print(max_xor([3, 10, 5, 25, 2, 8]))

# [0] → 0
#  Only one number, XOR is 0
print(max_xor([0]))

# [2, 4] → 6
#  2 ^ 4 = 6
print(max_xor([2, 4]))

# [8, 10, 2] → 10
#  8 ^ 2 = 10
print(max_xor([8, 10, 2]))

# [12, 15, 7, 9] → 14
print(max_xor([12, 15, 7, 9]))