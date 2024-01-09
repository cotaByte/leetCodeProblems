
"""
THIS  CORRESPONDS TO THE LIST OF PROBLEMS LEETCODE 75
1071. Greatest Common Divisor of Strings - Easy
For two strings s and t, we say "t divides s" if and only if s = t + ... + t 
(i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides
both str1 and str2.

 

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

"""
def gcdOfStrings( str1: str, str2: str) -> str:
    import math 
    if str1+str2 != str2+str1: return "" 
    else: return str1[:math.gcd(len(str1),len(str2))]




#str1 = "ABCABC"
#str2 = "ABC"

str1 = "ABABAB"
str2 = "ABAB"
 


print(gcdOfStrings(str1,str2))