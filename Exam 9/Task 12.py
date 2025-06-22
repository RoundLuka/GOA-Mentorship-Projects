# 12) Word Break Problem
"""
Instructions:
Given a string and a dictionary, determine if the string can be 
segmented into a space-separated sequence of dictionary words.
"""

def word_break(string, dict):
    for word in dict:
        string = string.replace(word, "")
    return string == ""

# Test Cases:
# "leetcode", dictionary ["leet","code"] → True
print(word_break( "leetcode", ["leet","code"]))

# "applepenapple", dict ["apple","pen"] → True
print(word_break( "applepenapple", ["apple","pen"]))

# "catsandog", dict ["cats","dog","sand","and","cat"] → False
print(word_break( "catsandog", ["cats","dog","sand","and","cat"]))