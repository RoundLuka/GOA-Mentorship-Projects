"""5. Given an array of integers, find all unique pairs of elements that sum to a given target number."""

def pairsSum(arr, target):
    res = []
    for i in range(len(arr)):

        for j in range(len(arr)):
            if i != j:
                if arr[i] + arr[j] == target:
                    pair = (arr[i], arr[j])
                    if pair[::-1] not in res:
                        res.append(pair)
    return list(set(res))

# Test Cases
# 5. [1, 2, 3, 2, 4], 5 -> [(1, 4), (2, 3)],    [1, 2, 3], 7 -> [],    [-1, 0, 1, 2, -2, 3], 0 -> [(-1, 1), (-2, 2)]

print(pairsSum([1, 2, 3, 2, 4], 5)) #  -> [(1, 4), (2, 3)]
print(pairsSum([1, 2, 3], 7)) #  -> []
print(pairsSum([-1, 0, 1, 2, -2, 3], 0)) #  -> [(-1, 1), (-2, 2)]