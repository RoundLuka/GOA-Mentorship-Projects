# 7) Find Pairs with Given Sum
"""
Instructions:
Write a function that returns all pairs of numbers from a list that add up to a given target sum.
"""

def all_pairs(arr, target):
    length = len(arr)
    result = []
    added = []
    for i in range(length):
        for j in range(length):
            if i != j:
                pair = (i, j)
                if arr[i] + arr[j] == target and pair not in added and pair[::-1] not in added:
                    result.append((arr[i], arr[j]))
                    added.append((i, j))
    return result


# Test Cases:
# [1,2,3,4], 5 → [(1,4),(2,3)]
print(all_pairs([1,2,3,4], 5))

# [0,0,1,1], 1 → [(0,1),(0,1)]
print(all_pairs([0,0,1,1], 1))

# [5,5,5], 10 → [(5,5),(5,5),(5,5)]
print(all_pairs([5,5,5], 10))

# [1], 2 → []
print(all_pairs([1], 2))

# [], 0 → []
print(all_pairs([], 0))