'''
@Author: your name
@Date: 2020-06-09 00:05:20
@LastEditTime: 2020-06-09 15:30:59
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/String/58.Length_of_Last_Word.py
'''
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a maximal substring consisting of non-space characters only.
''' 
Example:

Input: "Hello World"
Output: 5
'''

class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        return len(s.split(' ')[-1])
    
words = ["i", "love", "leetcode", "i", "love", "coding"]
count = collections.Counter(words)
[v[0] for v in sorted(count.items(),key=lambda x: (-x[1], x[0]))[:4]]
