"""7. Find All Prime Numbers in a Given Range

Task:
Write a function that takes two integers, start and end, and returns
a list of all prime numbers in the range [start, end]. A prime
number is a number greater than 1 that has no divisors other than 1
and itself.
"""

# defined secondary isPrime function to help detect if number is prime or not, as its very important part of the task

def isPrime(num):
    # checking if number gets evenly divided to divisors ranging 2 to itself
    for divisor in range(2, num):
        if num % divisor == 0:
            # if its evenly divided its not prime
            return False
    # if it didn't get evenly divded once, its prime
    return True
            

def primeRange(start, end):
    # any number under 1 is not considered prime
    if end <= 1:
        return []
    # initialized list to store the result
    primes = []
    # iterating over given range and checking every number, if its prime adding to the result
    for num in range(start, end):
        if isPrime(num):
            primes.append(num)
    return primes




# Test Cases:
# ● Input: start = 10, end = 20
# Output: [11, 13, 17, 19]
print(primeRange(10, 20))
# ● Input: start = 1, end = 10
# Output: [2, 3, 5, 7]
print(primeRange(1, 10))
# ● Input: start = 20, end = 30
# Output: [23, 29]
print(primeRange(20, 30))
# ● Input: start = 24, end = 25
# Output: []
print(primeRange(24, 25))
# ● Input: start = 1, end = 1
# Output: []
print(primeRange(1, 1))
