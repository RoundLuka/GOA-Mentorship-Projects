"""4. Write a function to return the nth number in the Fibonacci sequence. Solve it both recursively and iteratively."""

# Iterative solution

def nth_fibonnaci_literative(n):
    arr = [0, 1]
    for i in range(1, n ):
        current = arr[i - 1] + arr[i]
        arr.append(current)
    return arr[-1]

# Recursive solution

def nth_fibonnaci_recursive(n):
    if n <= 1:
        return n
    return nth_fibonnaci_recursive(n - 1) + nth_fibonnaci_recursive(n - 2)

# Test Cases
#4. 0 -> 0, 5 -> 5, 10 -> 55

# Literative

print(nth_fibonnaci_literative(0)) # -> 0
print(nth_fibonnaci_literative(5)) # -> 5
print(nth_fibonnaci_literative(10)) # -> 55

# Recursive

print(nth_fibonnaci_recursive(0)) # -> 0
print(nth_fibonnaci_recursive(5)) # -> 5
print(nth_fibonnaci_recursive(10)) # -> 55

