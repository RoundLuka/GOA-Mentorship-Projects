# 6) Sum Numbers in a String
"""
Instructions:
Write a function that finds all numbers in a string and returns their sum.
"""

def find_numbers_sum(string):
    digits = "0123456789"
    sum = 0
    length = len(string)

    for index in range(len(string)):
        if index > 1 and string[index - 1] in digits:
            continue

        char = string[index]
        if char in digits:
            number = ""
            next = 0

            while index + next < length and string[index + next] in digits:
                number += string[index + next]
                next += 1
            
            if len(number) > 1:
                sum += int(number)
            else:
                sum += int(char)
    return sum


# Test Cases:
# "abc123xyz" → 123
print(find_numbers_sum("abc123xyz"))

# "7 apples and 3 oranges" → 10
print(find_numbers_sum("7 apples and 3 oranges"))

# "no numbers" → 0
print(find_numbers_sum("no numbers"))

# "1a2b3c" → 6
print(find_numbers_sum("1a2b3c"))

# "100 200" → 300
print(find_numbers_sum("100 200"))