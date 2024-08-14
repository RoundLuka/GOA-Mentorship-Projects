"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N.

Test Cases:
[2, 4, 0, 100, 4, 11, 2602, 36] ->  11
[160, 3, 1719, 19, 11, 13, -21] -> 160
[7516484, 526386, 1637037, 813302, -8496994, 812820, 3797630, -3773758, 921354, 6123650, 1693668] -> 1637037
[8811272, 9218790, 9094178, -818772, 2711934, -3905606, 1332109] -> 1332109
[-4207752, 362590, 5205484, 11340, 3740336, 1360605] -> 1360605
"""

# Soultion

def outlier(arr):
    if arr[0] % 2 == 0 and arr[1] % 2 == 0:
        for num in arr:
            if num % 2 != 0:
                return num
    if arr[2] % 2 == 0:
        if arr[0] % 2 == 1:
            return arr[0]
        return arr[1]
    else:
        if arr[0] % 2 == 0:
            return arr[0]
        return arr[1]
    
# Test cases

print(outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(outlier([160, 3, 1719, 19, 11, 13, -21]))
print(outlier([7516484, 526386, 1637037, 813302, -8496994, 812820, 3797630, -3773758, 921354, 6123650, 1693668]))
print(outlier([8811272, 9218790, 9094178, -818772, 2711934, -3905606, 1332109]))
print(outlier([-4207752, 362590, 5205484, 11340, 3740336, 1360605]))

        
    


