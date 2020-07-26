'''
@Author: your name
@Date: 2020-07-01 16:15:14
@LastEditTime: 2020-07-01 16:22:35
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/14.DP/91.Decode_Ways.py
'''
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.

""" 
Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6). 
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        self.memo={}
        return self.helper(s)
    def helper(self,s):
        
        if len(s) == 0: 
            return 1
        if s in self.memo: 
            return self.memo[s]
        
        takeOne = takeTwo = 0
        
        if int(s[:1]) >= 1 and int(s[:1]) <= 9:
            takeOne = self.helper(s[1:])
            
        if int(s[:2]) >= 10 and int(s[:2]) <= 26:
            takeTwo = self.helper(s[2:])
        
        self.memo[s] = takeOne + takeTwo
        
        return self.memo[s]