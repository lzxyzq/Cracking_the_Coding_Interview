'''
@Author: your name
@Date: 2020-06-21 01:25:55
@LastEditTime: 2020-06-21 08:59:38
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Find/35.Search_Insert_Position.py
'''
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.
""" Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""
# Method 1 
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)==0: return 0
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)

# Time :O(n)
# Space :O(1)

# Method 2
class Solution:
    def searchInsert(self, nums: List[int], target: int) :
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right :
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left

# Time :O(logn)
# Space :O(1)