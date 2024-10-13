"""2. Write a function to find the longest common prefix among an array of strings. If there is no common prefix, return an empty string."""

def longestPrefix(arr):
    res = ""
    while True:
        for i in range(len(arr)):
            current_char = ""
            counter = 0
            for j in range(len(i)):
                current_char = i[j]
                if counter == len(current_char):
                    break
                counter += 1
            # unfinished






# Test Cases
# ["flower", "flow", "flight"] -> "fl", ["dog", "racecar", "car"] -> "", ["apple", "apple", "apple"] -> "apple"

print(longestPrefix(["flower", "flow", "flight"])) # -> fl
print(longestPrefix(["dog", "racecar", "car"])) #  -> ""
print(longestPrefix(["apple", "apple", "apple"])) #  -> "apple"
