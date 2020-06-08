'''
@Author: your name
@Date: 2020-06-01 18:51:30
@LastEditTime: 2020-06-01 19:27:30
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Array/16.3Sum_Closest.py
'''
# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

''' Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self, nums, target) :
        diff = float('inf')
        nums.sort()
        for i in range (len(nums)-2):
            lo , hi = i + 1 , len(nums) - 1
            while (lo < hi) : 
                Sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - Sum) < abs(diff):
                    diff = target -Sum
                if Sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0: 
                break
        return target - diff
        
# Complexity Analysis
# https://leetcode.com/problems/3sum-closest/solution/