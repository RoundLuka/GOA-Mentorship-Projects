"""Task 6: Count Substring Occurrences
Write a function count_substring(text, sub) that returns how many times a substring sub occurs in text (overlaps allowed).
"""

def count_substring(text, sub):
    length = len(text)
    count = 0
    for i in range(length):
        for j in range(length):
            try:
                if text[i:j + 1] == sub:
                    count += 1
            except:
                if text[i:j] == sub:
                    count += 1
    return count


# Test Cases:
print(count_substring("aaaa", "aa") == 3)
print(count_substring("hello hello", "lo") == 2)
print(count_substring("banana", "ana") == 2)