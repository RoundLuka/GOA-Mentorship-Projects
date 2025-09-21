"""3. Reverse the Order of Words in a Sentence

Task:
Write a function that takes a sentence and reverses the order of its words.
"""

def reverseOrder(sentence):
    # splitting sentence into list of words
    words = sentence.split()
    # reversing the list
    reversed_words = words[::-1]
    # combining all the words back into sentence with " " separator between them
    return " ".join(reversed_words)

# Test Cases:
# 1. Input: "Hello World" → Output: "World Hello"
print(reverseOrder("Hello World"))
# 2. Input: "Python is great" → Output: "great is Python"
print(reverseOrder("Python is great"))
# 3. Input: "a b c" → Output: "c b a"
print(reverseOrder("a b c"))
# 4. Input: "" → Output: ""
print(reverseOrder(""))
# 5. Input: " Spaces " → Output: "Spaces"
print(reverseOrder(" Spaces "))