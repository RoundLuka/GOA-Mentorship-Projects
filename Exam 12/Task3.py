"""
Task 3: Remove Punctuation
Write a function remove_punctuation(s) that removes all punctuation characters from a string.
"""

def remove_punctuation(s):
    punctuation = ".,:'""!?/;`"
    
    result = ""

    for char in s:
        if char not in punctuation:
            result += char

    return result

# Test Cases:
print(remove_punctuation("Hello, world!") == "Hello world")
print(remove_punctuation("Python: easy? Yes!") == "Python easy Yes")