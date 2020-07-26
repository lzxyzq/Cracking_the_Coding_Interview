'''
@Author: your name
@Date: 2020-06-09 17:21:16
@LastEditTime: 2020-06-10 12:19:27
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/String/290.Word_Pattern.py
'''
# Given a pattern and a string str, find if str follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

''' 
Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false 
'''

# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.


# 1.split()
# 2.等长len()
# 3.hashmap key:pattern value:str
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.split()
        result = ''
        if len(str) != len(pattern):
            return False
        d = {}
        for i in range(len(pattern)):
            if str[i] not in d:
                if pattern[i] not in d.values():
                    d[str[i]] = pattern[i]
                else:
                    return False
            result += d[str[i]]
        return result == pattern
       

pattern = "abba"
str = "dog cat cat dog"
words = str.split(' ')
tuple(zip(words, pattern))