"""
Write python program that will turn decimal number into binary number.

Test Cases:
32 -> 100000
31 -> 11111
8 -> 1000
"""

# Solution

def to_binary(dec):
    res = []
    while dec > 0:
        remainder = dec % 2
        res.append(str(remainder))
        dec = dec // 2
    return "".join(res[::-1])

# Test cases

print(to_binary(32))
print(to_binary(31))
print(to_binary(8))