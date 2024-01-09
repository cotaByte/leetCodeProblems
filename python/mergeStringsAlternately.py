"""
THIS  CORRESPONDS TO THE LIST OF PROBLEMS LEETCODE 75
1768. Merge Strings Alternately
Easy
You are given two strings word1 and word2. Merge the strings by adding letters 
in alternating order, starting with word1. If a string is longer than the other,
append the additional letters onto the end of the merged string.

Return the merged string.
 

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s


Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.

"""


def mergeAlternately(word1:str,word2:str)->str:
    
    w1=list(word1)
    w2=list(word2)
    l= max(len(w1),len(w2))
    merge=[]
    k=0
    
    for i in range(l):
        if i<len(w1):
            merge.append(w1[i])
            k+=1
        if i<len(w2):
            merge.append(w2[i])
            k+=1
            
    return ''.join(merge)            
    
    
word1 = "abcd"
word2 = "pq"
    

m=mergeAlternately(word1,word2)
print(m)
    
    
    
    
    
    
    
    