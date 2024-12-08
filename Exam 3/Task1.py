"""1. Check If Two Strings Are Anagrams

Task:
Write a function that determines if two strings are anagrams of each other.
"""


def detectAnagram(word1, word2):
    # lowering both words as this task is case insenseitive
    word1 = word1.lower()
    word2 = word2.lower()
    # returning boolean value, checking if both strings contain same letters
    return sorted(word1) == sorted(word2)


# Test Cases:
# 1. Input: ("listen", "silent") → Output: True
print(detectAnagram("listen", "silent"))
# 2. Input: ("triangle", "integral") → Output: True
print(detectAnagram("triangle", "integral"))
# 3. Input: ("apple", "pale") → Output: False
print(detectAnagram("apple", "pale"))
# 4. Input: ("a", "a") → Output: True
print(detectAnagram("a", "a"))
# 5. Input: ("rat", "car") → Output: False
print(detectAnagram("rat", "car"))