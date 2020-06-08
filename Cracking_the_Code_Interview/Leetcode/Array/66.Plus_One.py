'''
@Author: your name
@Date: 2020-06-02 22:22:55
@LastEditTime: 2020-06-02 22:22:55
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Array/66.Plus_One.py
'''
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

''' Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

class Solution:
    def plusOne(self, digits):
        s = ''.join(str(i) for i in digits)
        s = str(int(s) + 1)
        print(s)
        return s

# -----------------------------------------------------------------
class Solution:
    def plusOne(self, digits):
        num = 0 
        for d in digits:
            num *= 10 
            num += d
        num += 1
        result = []
        
        while num:
            temp = num % 10
            num //= 10
            result.append(temp)
        return result[::-1]
        