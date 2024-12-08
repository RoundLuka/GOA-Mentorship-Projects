"""2. Count the Number of Unique Words in a Text

Task:
Write a function that counts the number of unique words in a string, ignoring case sensitivity
and punctuation.
"""

def wordCount(sentence):
    # lowering entire sentence as this task is case insenseitive
    sentence = sentence.lower()
    # getting rid of punctuation
    sentence = sentence.replace(".", "").replace(",", "").replace(":", "").replace("!","").replace("?", "")
    # splitting sentence into array of words
    words = sentence.split()
    filtered = []
    # removing duplicate words
    for word in words:
        if word not in filtered:
            filtered.append(word)
    # returning value of unique words 
    return len(filtered)


# Test Cases:
# 1. Input: "The quick brown fox jumps over the lazy dog" → Output: 8
print(wordCount("The quick brown fox jumps over the lazy dog"))
# 2. Input: "Hello hello world!" → Output: 2
print(wordCount("Hello hello world!"))
# 3. Input: "" → Output: 0
print(wordCount(""))
# 4. Input: "Python is fun. Python is cool." → Output: 4
print(wordCount("Python is fun. Python is cool."))
# 5. Input: "One word" → Output: 2
print(wordCount("One word"))
