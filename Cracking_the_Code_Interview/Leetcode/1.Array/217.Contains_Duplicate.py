'''
@Author: your name
@Date: 2020-06-03 14:39:41
@LastEditTime: 2020-06-03 15:19:44
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Array/217.Contains_Duplicate.py
'''
# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

''' Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
class Solution:
    def containsDuplicate(self, nums):
        return True if len(set(nums)) < len(nums) else False
# -----------------------------------------------------------
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = set()
        for i in nums:
            if i in result:
                return True
            result.add(i)
        return False