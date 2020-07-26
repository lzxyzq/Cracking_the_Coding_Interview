'''
@Author: your name
@Date: 2020-06-10 12:23:43
@LastEditTime: 2020-06-10 13:20:06
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/String/242.Valid_Anagram.py
'''
# Given two strings s and t , write a function to determine if t is an anagram of s.
''' 
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
'''
# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str):
        return Counter(s)==Counter(t)

# ---------------------------------
class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s)!=len(t):
            return False
        
        dictS, dictT = {}, {}
        for _i in s:
            if _i not in dictS:
                dictS[_i]=1
            else:
                dictS[_i]+=1
        for _i in t:
            if _i not in dictT:
                dictT[_i]=1
            else:
                dictT[_i]+=1
        
        for _i in dictS:
            if _i not in dictT:
                return False
            if dictS[_i]!=dictT[_i]:
                return False
        return True