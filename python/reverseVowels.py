"""
THIS  CORRESPONDS TO THE LIST OF PROBLEMS LEETCODE 75

345. Reverse Vowels of a String - Easy
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in 
both lower and upper cases, more than once.

 

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
 

Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

"""
def reverseVowels(s):
    
    array_s=list(s)
    vowels=['a','e','i','o','u']
    vowels+=[item.upper() for item in vowels]
    
    matches = {index: char for index, char in enumerate(s) if char in vowels}
    rev= dict(zip(matches, reversed(list(matches.values()))))
    
    for key, value in rev.items(): array_s[key]=value
    
    return ''.join(array_s)
    
s="leetcode"

s_final=reverseVowels(s)
print(s_final)