"""Task 1: Sorting by Frequency
Write a function sort_by_frequency(lst) that returns the list sorted by frequency of elements (most frequent first). If two numbers have the same frequency, keep the smaller number first.
"""

def sort_by_frequency(lst):
    item_frequency = {}

    for item in lst:
        item_frequency[item] = lst.count(item)

    sorted_items = item_frequency.items()
    sorted_items = sorted(sorted_items, key=lambda x: x[1])[::-1]

    result = []

    for value, multiplier in sorted_items:
        for i in range(multiplier):
            result.append(value)
    return result


# Test Cases:
print(sort_by_frequency([4,4,1,2,2,3,3,3]) == [3,3,3,2,2,4,4,1])
print(sort_by_frequency([10,20,10,30,20,10]) == [10,10,10,20,20,30])
print(sort_by_frequency([]) == [])