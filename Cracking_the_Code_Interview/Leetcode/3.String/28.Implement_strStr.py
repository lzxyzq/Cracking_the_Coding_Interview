'''
@Author: your name
@Date: 2020-06-08 15:28:39
@LastEditTime: 2020-06-08 18:52:10
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/String/28.Implement_strStr.py
'''
# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
''' Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''
class Solution:
    def strStr(self, haystack, needle):
        i = j = 0
        if len(needle) == 0:
            return 0 
        
        while i < len(haystack):
            if i < len(haystack) and haystack[i] == needle[j]:
                j += 1
            else:
                i -= j
                j = 0
            i += 1
            if len(needle) == j:
                return i - j 
        return -1 

# ----------------------------------------------------------------
class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

# -----------------------------------------------------------------
class Solution:
    def strStr(self, haystack, needle) :
        if len(needle) == 0 : 
            return 0
        return haystack.find(needle)