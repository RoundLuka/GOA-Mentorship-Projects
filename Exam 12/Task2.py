"""Task 2: Decode Run-Length Encoding
Write a function decode_rle(s) that decodes a run-length encoded string.
Example: "a3b2c1" → 'aaabbc'"""

def decode_rle(s):
    digits = "0123456789"
    result = ""


    for index in range(len(s)):

        if index > 0:
            char = s[index - 1]
            multiplier = s[index]
            if multiplier in digits:
                result += char * int(s[index])
    return result

# Test Cases:
print(decode_rle("a3b2c1") == "aaabbc")
print(decode_rle("x5y1") == "xxxxxy")
print(decode_rle("") == "")