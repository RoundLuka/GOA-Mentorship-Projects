# 5) Check for Armstrong Number
"""
Instructions:
An Armstrong number is one whose sum of the nth power of its digits equals the number itself.
Write a function to check for this.
"""

def check_amstrong(number):
    power = len(str(number))

    digit_sum = 0
    for digit in str(number):
        digit_sum += int(digit) ** power
    
    return digit_sum == number


# Test Cases:
# 153 → True (1³ + 5³ + 3³ = 153)
print(check_amstrong(153))
# 370 → True (3³ + 7³ + 0³ = 370)
print(check_amstrong(370))
# 9474 → True (9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474)
print(check_amstrong(9474))
# 10 → False (1² + 0² = 1 ≠ 10)
print(check_amstrong(10))
# 1 → True (1¹ = 1)
print(check_amstrong(1))