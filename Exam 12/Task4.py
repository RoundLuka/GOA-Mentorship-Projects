"""
Task 4: Intersection of Two Dictionaries
Write a function dict_intersection(d1, d2) that returns a dictionary containing keys that appear in both dictionaries, with their values summed.
"""

def dict_intersection(d1, d2):
    res = {}
    d2_keys = d2.keys()
    for key, value in d1.items():
        if key in d2_keys:
            res[key] = value + d2[key]
    return res

# Test Cases:
print(dict_intersection({"a":1,"b":2},{"b":3,"c":4}) == {"b":5})
print(dict_intersection({"x":10},{"y":5}) == {})