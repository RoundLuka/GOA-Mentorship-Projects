"""Task 5: Remove Consecutive Duplicates
Write a function remove_consecutive_duplicates(s) that removes consecutive duplicate characters from a string.
"""

def remove_consecutive_duplicates(s):
    res = ""
    for index in range(len(s)):
        try:
            if s[index] != s[index + 1]:
                res += s[index]
        except:
            res += s[index]
    return res


# Test Cases:
print(remove_consecutive_duplicates("aaabbcddd") == "abcd")
print(remove_consecutive_duplicates("hellooo") == "helo")
print(remove_consecutive_duplicates("abc") == "abc")