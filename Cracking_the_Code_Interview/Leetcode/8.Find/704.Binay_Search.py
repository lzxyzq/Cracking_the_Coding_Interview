'''
@Author: your name
@Date: 2020-06-22 02:03:38
@LastEditTime: 2020-06-22 02:04:39
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Find/704.Binay_Search.py
'''

# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.
"""
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid -1 
            else:
                lo = mid + 1
        return -1 


# Time: O(logn)
# Space: O(1)