"""9. Primorial of a Number

Task:
Write a function that calculates the primorial of a number. The primorial of a number n is
the product of all prime numbers less than or equal to n. For example, the primorial of 5 is
the product of the primes less than or equal to 5: 2 * 3 * 5 = 30.
Your function should take an integer n and return the primorial of that number."""

def isPrime(num):
    # checking if number gets evenly divided to divisors ranging 2 to itself
    for divisor in range(2, num):
        if num % divisor == 0:
            # if its evenly divided its not prime
            return False
    # if it didn't get evenly divded once, its prime
    return True

def primorial(n):
    # initializing variable to store values
    product = 1
    # starting iterating from 2 as any numbers under it aren't considered prime and ending it with the number itself
    for num in range(2, n + 1):
        # checking if each number is prime
        if isPrime(num):
            product *= num
    return product


# Test Cases:
# ● Input: n = 5
# Output: 30
# Explanation: The prime numbers less than or equal to 5 are 2, 3, and 5. Their product
# is 2 * 3 * 5 = 30.
print(primorial(5))
# ● Input: n = 10
# Output: 210
# Explanation: The prime numbers less than or equal to 10 are 2, 3, 5, and 7. Their
# product is 2 * 3 * 5 * 7 = 210.
print(primorial(10))
# ● Input: n = 1
# Output: 1
# Explanation: There are no primes less than or equal to 1, so the primorial is 1 by
# definition.
print(primorial(1))
# ● Input: n = 7
# Output: 210
# Explanation: The prime numbers less than or equal to 7 are 2, 3, 5, and 7. Their
# product is 2 * 3 * 5 * 7 = 210.
print(primorial(7))
# ● Input: n = 11
# Output: 2310
# Explanation: The prime numbers less than or equal to 11 are 2, 3, 5, 7, and 11. Their
# product is 2 * 3 * 5 * 7 * 11 = 2310.
print(primorial(11))