"""10. Sum Fractions Using GCD and LCM

Task:
Write a function that sums two fractions and returns the result in its simplest form. The
fractions will be given as two tuples, where each tupleconsists of two integers:  the
numerator and the denominator. To simplify the result, you need to compute the Least
Common Multiple (LCM) and Greatest Common Divisor (GCD) of the denominators.
Then, simplify the result by dividing both the numerator and denominator by their GCD.
To calculate the Greatest Common Divisor (GCD) of two numbers in Python, you can use
the Euclidean algorithm, which is an efficient way to find the GCD. Here's an explanation of
how to build the GCD function and how the algorithm works:
Understanding the Euclidean Algorithm
The Euclidean algorithm finds the GCD of two integers a and b by repeatedly applying the
following steps:
1. Divide aby band calculate the remainder (a % b).
2. Replace a with b and b with the remainder from the previous step.
3. Repeat the process until the remainder becomes 0. The GCD will be the last
non-zero value of b.
Steps to Build GCD Function in Python
1. Initial Check: If b becomes 0, then a is the GCD.
2. Iterate: Continue the division and remainder operation until the remainder becomes
0.
Understanding and Building LCM (Least Common Multiple) in Python
The Least Common Multiple (LCM) of two integers is the smallest positive integer that is
divisible by both numbers. The relationship between the LCM and GCD of two numbers can
be used to efficiently compute the LCM.
LCM(a, b) = |a * b| / GCD(a, b)"""


# gcd algorithm, not in use
#     while b1 != 0:
#         temp = b1
#         b1 = a1 % b1
#         a1 = temp


# gcd algorithm reccursion way
def gcd(x, y):
    return y == 0 and x or gcd(y, x % y)


def sum_fractions(frac1, frac2):
    # fractions, split into 2 variables, 0 index for numerator, 1 index for denominator

    # first fraction - a
    a0 = frac1[0]
    a1 = frac1[1]

    # second fraction - b
    b0 = frac2[0]
    b1 = frac2[1]
    

    # calling gcd function and finding Greatest Common Divisor (GCD)
    GCD = gcd(a1, b1)

    # calculating the Least Common Multiple (LCM), for denominators
    LCM = (a1 * b1) // GCD

    # raising numerators by same ratio as denominators

    a0 = (LCM // a1) * a0
    b0 = (LCM // b1) * b0

    # summing up numerators
    numerator = a0 + b0
    
    # Least Common Multiple (LCM), for denominators now is common dominator
    denominator = LCM

    whil
    
    return (numerator, denominator)
    


# Test Cases:
# ● Input: frac1 = (1, 2), frac2 = (1, 3)
# Output: (5, 6)
# Explanation: The LCM of 2 and 3 is 6. The sum is (1 * 3) / 6 + (1 * 2) / 6
# = 3/6 + 2/6 = 5/6.
print(sum_fractions(frac1 = (1, 2), frac2 = (1, 3)))
# ● Input: frac1 = (1, 4), frac2 = (1, 4)
# Output: (1, 2)
# Explanation: The LCM of 4 and 4 is 4. The sum is (1/4 + 1/4) = 2/4 = 1/2.
print(sum_fractions((1, 4), frac2 = (1, 4)))
# ● Input: frac1 = (2, 5), frac2 = (1, 5)
# Output: (3, 5)
# Explanation: The LCM of 5 and 5 is 5. The sum is (2/5 + 1/5) = 3/5.
print(sum_fractions(frac1 = (2, 5), frac2 = (1, 5)))
# ● Input: frac1 = (3, 4), frac2 = (5, 6)
# Output: (19, 12)
# Explanation: The LCM of 4 and 6 is 12. The sum is (3 * 3) / 12 + (5 * 2) /
print(sum_fractions((3, 4), frac2 = (5, 6)))
# 12 = 9/12 + 10/12 = 19/12.
# ● Input: frac1 = (5, 12), frac2 = (7, 15)
# Output: (139, 60)
# Explanation: The LCM of 12 and 15 is 60. The sum is (5 * 5) / 60 + (7 * 4)
# / 60 = 25/60 + 28/60 = 53/60.
print(sum_fractions((5, 12), frac2 = (7, 15)))