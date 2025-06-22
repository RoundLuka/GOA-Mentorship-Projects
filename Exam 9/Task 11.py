# 11) Minimum Window Substring
"""
Instructions:
Given two strings s and t, find the minimum substring in s which contains all characters of t.
"""

def manual_sort_assist(string):
    arr = sorted(string)
    result = ""
    for char in arr:
        result += char
    return result

def minimum_window(s, t):
    length = len(s)

    # if len(t) > length:
    #     return ""
    found = False
    shortest = s
    for index in range(length):
        for j in range(index, length):
            current = s[index: j + 1]
            if manual_sort_assist(t) in manual_sort_assist(current) and len(current) < len(shortest):
                shortest = current
                found = True
    if not found and s != t: 
        return ""
    return shortest
        
        

# Test Cases:
# s="ADOBECODEBANC", t="ABC" → "BANC"
print(minimum_window("ADOBECODEBANC", "ABC"))

# s="a", t="a" → "a"
print(minimum_window("a", "a"))

# s="a", t="aa" → ""
print(minimum_window("a", "aa"))

# s="ab", t="b" → "b"
print(minimum_window("ab", "b"))