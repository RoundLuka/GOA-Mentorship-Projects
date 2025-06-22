# 9) Find Longest Palindromic Substring
"""
Instructions:
Write a function that finds the longest palindromic substring in a given string.
"""

def longest_palindrome(string):
    if string[::-1] == string:
        return string

    length = len(string)
    longest = ""
    for i in range(length):
        for j in range(length):
            if i != j:
                current = string[i:j]
                if current == current[::-1] and len(current) > len(longest):
                    longest = current
    return longest

    
# Test Cases:
# "babad" → "bab" or "aba"
print(longest_palindrome("babad"))

# "cbbd" → "bb"
print(longest_palindrome("cbbd"))

# "a" → "a"
print(longest_palindrome("a"))

# "" → ""
print(longest_palindrome(""))

# "forgeeksskeegfor" → "geeksskeeg"
print(longest_palindrome("forgeeksskeegfor"))