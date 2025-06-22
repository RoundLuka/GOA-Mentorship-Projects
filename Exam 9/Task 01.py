# 1) Sum Digits Until Single Digit
"""Instructions:
Write a function that takes a non-negative integer and returns the sum of its digits. If the result has more than one digit, repeat the process until the result is a single digit.
"""

def digit_sum(positive_integer):

    while len(str(positive_integer)) != 1:
        sum_of_digits = 0
        for digit in str(positive_integer):
            sum_of_digits += int(digit)

        positive_integer = sum_of_digits
    
    return positive_integer

# Test Cases:
# 123 → 6
print(digit_sum(123))
# 0 → 0
print(digit_sum(0))
# 9999 → 9
print(digit_sum(9))
# 45 → 9
print(digit_sum(9))
# 1 → 1
print(digit_sum(1))
