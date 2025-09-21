"""
Task 10: Longest Consecutive Characters
Write a function longest_consecutive_char(s) that returns the longest run of the same character.
"""

def longest_consecutive_char(s):
    
    longest = 0
    current = 0
    symbol = ""
    for i in range(len(s)):
        char = s[i]
        try:
            if char == s[i + 1]:
                current += 1
            else:
                if current >= longest:
                    longest = current
                    symbol = char
                    current = 0
        except:  
            if current > longest:
                return (char, current + 1)

            if len(s) != 0:
                return (symbol, longest + 1)
            return (symbol, longest)
    if len(s) != 0:
        return (symbol, longest + 1)
    return (symbol, longest)


# Test Cases:
print(longest_consecutive_char("aaabbbaaac") == ("a",3))
print(longest_consecutive_char("bbbbb") == ("b",5))
print(longest_consecutive_char("") == ("",0))