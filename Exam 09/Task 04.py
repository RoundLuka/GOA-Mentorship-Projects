# 4) Implement a Simple Caesar Cipher
"""
Instructions:
Write a function that takes a message and a shift value and returns the message with each letter shifted (A→B, B→C, etc). 
Ignore non-alphabet characters.
"""

def case_cipher(message, shift):
    alphabet1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    for char in message:
        if char in alphabet1:
            position = alphabet1.index(char)
            res += alphabet1[position + shift]
        elif char in alphabet2:
            position = alphabet2.index(char)
            res += alphabet2[position + shift]
        else:
            res += char
    return res


# Test Cases:
# "abc", 1 → "bcd"
print(case_cipher("abc", 1))

# "xyz", 2 → "zab"
print(case_cipher("xyz", 2))

# "Hello!", 3 → "Khoor!"
print(case_cipher("Hello!", 3))

# "ABC", 1 → "BCD"
print(case_cipher("ABC", 1))

# "Test 123", 4 → "Xiwx 123"
print(case_cipher("Test 123", 4))