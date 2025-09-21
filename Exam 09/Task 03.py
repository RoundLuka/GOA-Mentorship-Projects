# 3) Find All Unique Substrings of a String
"""
Instructions:
Write a function that takes a string and returns a list of all unique substrings.
"""

def unique_substrings(string):
    length = len(string)
    result = []
    for index in range(length):
        
        for index2 in range(length):
            if index == index2 and string[index] not in result:
                result.append(string[index])
            else:
                substring = string[index:index2 + 1]
                if substring != "" and substring not in result:
                    result.append(substring)
    return result


# Test Cases:
# "abc" → ["a","ab","abc","b","bc","c"]
print(unique_substrings("abc"))

# "a" → ["a"]
print(unique_substrings("a"))

# "ab" → ["a","ab","b"]
print(unique_substrings("ab"))

# "" → []
print(unique_substrings(""))

# "aa" → ["a","aa"]
print(unique_substrings("aa"))
