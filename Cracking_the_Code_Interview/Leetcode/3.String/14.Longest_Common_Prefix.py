'''
@Author: your name
@Date: 2020-06-13 23:44:53
@LastEditTime: 2020-06-14 09:36:09
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/String/14.Longest_Common_Prefix.py
'''
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ''
        m, M = min(strs), max(strs)
        for i, letter in enumerate(m):
            if letter != M[i]:
                return m[:i]
        return m

