'''
@Author: your name
@Date: 2020-06-09 18:11:07
@LastEditTime: 2020-06-09 18:11:08
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/String/205.Isomorphic_Strings.py
'''
# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) == len(set(t)):
            m = {}
            for i in range(len(s)):
                if s[i] not in m:
                    m[s[i]] = t[i]
                else:
                    if t[i] != m[s[i]]:
                        return False
            return True
        return False