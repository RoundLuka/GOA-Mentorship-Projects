"""
Write an algorithm in python to count the number of capital letters in
a string. How many comparisons does it do? What is the fewest num-
ber of increments it might do? What is the largest number? (Use N for the
number of characters in the file when writing your answer.)
"""

# Solution

def capital_count(string):
    count = 0
    for char in string:
        if char == char.capitalize():
            count += 1
    return count


# Answers

# How many comparisons does it do?
# If we assign N to length of string, or amount of characters in string then
# algorithm will do N comparsions, as every character is being compared to
# its capitalized version

# What is the fewest number of increments it might do?
# Fewest number of increments algorithm might do is 0, because it only
# does increment when there is capital letter in string, if there were
# to be 0 capital letters in string, algorithm would do 0 increments

# What is the largest number of increments it might do?
# Largest number of increments algorithm might do is N, if we assign N
# to be length of string or amount of characters. That would be worst
# case when all of letters in string are capital, uppercase.
