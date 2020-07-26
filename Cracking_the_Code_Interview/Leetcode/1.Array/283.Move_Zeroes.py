'''
@Author: your name
@Date: 2020-06-02 10:25:18
@LastEditTime: 2020-06-02 10:31:24
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Array/Move_Zeroes.py
'''
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

''' Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0] 
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt] = nums[i]
                lastNonZeroFoundAt += 1
        for j in range(lastNonZeroFoundAt,len(nums)):
            nums[j] = 0

