"""
4. Find All Anagrams in a String
Given a string s and a string p, return the starting indices of all anagrams of p in s.
Input:
A string s (length ≤ 10⁵).
A string p (length ≤ 10⁴).
Output: boolean - True if they are anagrams, otherwise False.
"""

def anagrams(s, p):
    return sorted(s) == sorted(p)

print(anagrams("abc", "bcd"))
print(anagrams("luka", "world"))