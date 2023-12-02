import math
"""

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit
integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers
(signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231


"""
def reverse(x):
    
    num=abs(x)
    if num==0 or num > pow(2,31): return 0
    
    negative = -1 if x<0 else 1
    rev=[]
    
    while (num!=0 ):
        rev.append(num%10)
        num=math.floor(num/10);
    
    n=negative * int(''.join(map(str,rev)))  
    return 0 if abs(n)>pow(2,31) else n

    


    
number_reversed= reverse(-120)
print(number_reversed)
