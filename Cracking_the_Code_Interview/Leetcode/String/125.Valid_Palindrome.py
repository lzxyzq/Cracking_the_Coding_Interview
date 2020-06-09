'''
@Author: your name
@Date: 2020-06-07 22:32:11
@LastEditTime: 2020-06-07 22:32:51
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/String/125.Valid_Palindrome.py
'''
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.

''' Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false 
'''

class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        s = [char for char in s if char.isalnum()]
        return s == s[::-1]