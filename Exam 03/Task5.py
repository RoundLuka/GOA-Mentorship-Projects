"""5. Encrypt and Decrypt Strings Using Caesar Cipher

Task:
Write a function to encrypt strings using a Caesar cipher with a given shift value.
"""

def encrypt(string, value):
    # initalizing double alphabet string and result variables
    letters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    res = ""
    # iterating over given string and then letters manually
    for char in string:
        if char in letters:
            # getting value of current char
            low = char.lower()
            current = string.index(low)
            # handling case
            if char == char.upper():
                res += (letters[current + value]).upper()
            else:
                res += letters[current + value]
        else:
            # char isn't alphabetic and is punctuaction mark then just adding it
            res += char
    # returning the result
    return res

# Test Cases:
# 1. Input: ("abc", 2) → Output: "cde"
print(encrypt("abc", 2))
# 2. Input: ("xyz", 3) → Output: "abc"
print(encrypt("xyz", 3))
# 3. Input: ("Hello, World!", 5) → Output: "Mjqqt, Btwqi!"
print(encrypt("Hello, World!", 5))
# 4. Input: ("Python", 0) → Output: "Python"
print(encrypt("Python", 0))
# 5. Input: ("abc", -1) → Output: "zab"
print(encrypt("abc", -1))