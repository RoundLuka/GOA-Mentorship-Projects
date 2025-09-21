"""8. Xbonacci Sequence

Task:
Write a function that generates the Xbonacci sequence. The Xbonacci sequence is a
generalization of the Fibonacci sequence, where each number is the sum of the previous X
numbers in the sequence.
For example, if X = 3 and the initial sequence is [1, 1, 1], the sequence will proceed as
follows:
● The 4th number is the sum of the previous 3: 1 + 1 + 1 = 3.
● The 5th number is the sum of the previous 3: 1 + 1 + 3 = 5.
● The 6th number is the sum of the previous 3: 1 + 3 + 5 = 9.
Your function should take two arguments:
1. X: The number of previous terms to sum.
2. n: The number of terms to generate."""

# Defined serperate function "last_sum" to assist with main function, with summing last x numbers. choose this way as I couldn't reset sum variable outside of loop code block in main function, this function takes 2 parameters, what term of last number it has to sum from array and array itself
def last_sum(x, arr):
    # initializing variables to count how many last number it has summed and sum itself
    count = 0
    sum = 0
    # iterating over reversed array, because we are specifically looking for last numbers
    for num in arr[::-1]:
        sum += num
        count += 1
        # if it has summed x term of number loop breaks
        if count == x:
            break
    # and finally returning sum to the main function
    return sum

def xbonacci(x, n):
    # manually checking for numbers under 3
    if x <= 3:
        if x == 1:
            return [1]
        elif x == 2:
            return [1,1]
        elif x == 3:
            return [1,1,1]
    # initializing starting array
    arr = []
    for i in range(x):
        arr.append(1)
    # subtracting x from n as first x numbers are in array
    for i in range(n - x):
        # for array length, calling function on each iteration
        current_sum = last_sum(x, arr)
        # appending given sum to number
        arr.append(current_sum)
    # returning the result
    return arr


# Test Cases:
# ● Input: X = 3, n = 10
# Output: [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
# Explanation: The first 10 numbers of the Xbonacci sequence starting with [1, 1,
# 1] and X = 3.
print(xbonacci(3, 10))
# ● Input: X = 2, n = 10
# Output: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Explanation: This is the Fibonacci sequence, where each number is the sum of the
# previous two numbers.
print(xbonacci(2, 10))
# ● Input: X = 4, n = 6
# Output: [1, 1, 1, 1, 4, 7]
# Explanation: Starting with [1, 1, 1, 1], the next terms are calculated by
# summing the last 4 terms.
print(xbonacci(4, 6))
# ● Input: X = 5, n = 8
# Output: [1, 1, 1, 1, 1, 5, 9, 17]
# Explanation: The sequence starts with five 1s, and each subsequent number is the
# sum of the previous 5 numbers.
print(xbonacci(5, 8))
# ● Input: X = 3, n = 1
# Output: [1]
# Explanation: Only one term in the sequence is required, so the output is [1].
print(xbonacci(3, 1))