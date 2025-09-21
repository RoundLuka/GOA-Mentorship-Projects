# 2) Convert a List to a Dictionary
"""Instructions:
Write a function that converts a list of key-value pair tuples into a dictionary.
"""

def dictionarize(arr):
    res = {}
    for pair in arr:
        res[pair[0]] = pair[1]
    return res

# Test Cases:
# [('a', 1), ('b', 2)] → {'a': 1, 'b': 2}
print(dictionarize([('a', 1), ('b', 2)]))

# [] → {}
print(dictionarize([]))

# [('x', 10)] → {'x': 10}
print(dictionarize([('x', 10)]))

# [('a', 1), ('a', 2)] → {'a': 2}
print(dictionarize([('a', 1), ('a', 2)]))

# [('one', 1), ('two', 2)] → {'one': 1, 'two': 2}
print(dictionarize([('one', 1), ('two', 2)]))