"""
You will be given a number and you will need to return it as a string in Expanded Form

Test Cases:
70304 -> '70000 + 300 + 4'
42 -> '40 + 2'
710163 -> '700000 + 10000 + 100 + 60 + 3'
853546 -> '800000 + 50000 + 3000 + 500 + 40 + 6'
511604 -> '500000 + 10000 + 1000 + 600 + 4'
"""

# Solution

def expanded(number):
    number = str(number)[::-1]
    res = []
    for i in range(len(number)):
        if number[i] != "0":
            num = number[i] + "0" * i
            res.append(num)
    return " + ".join(res[::-1])



# Test cases

print(expanded(70304))
print(expanded(42))
print(expanded(710163))
print(expanded(853546))
print(expanded(511604))