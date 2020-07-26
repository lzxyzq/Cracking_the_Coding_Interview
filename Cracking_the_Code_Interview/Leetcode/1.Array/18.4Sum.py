'''
@Author: your name
@Date: 2020-06-01 19:41:47
@LastEditTime: 2020-06-02 16:21:18
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Array/18.4Sum.py
'''
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:
# The solution set must not contain duplicate quadruplets.

''' Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums) - 2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1 
                right = len(nums) -1 
                while(left < right):
                    Sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if Sum < target:
                        left += 1
                    elif Sum > target:
                        right -= 1
                    else:
                        temp = []
                        temp.append(nums[i])
                        temp.append(nums[j])
                        temp.append(nums[left])
                        temp.append(nums[right])
                        result.append(temp)
                        left += 1
                        right -= 1
                        # skip duplicate value
                        while(left < right and nums[left] == nums[left-1]):
                            left += 1
                        while(left < right and nums[right] == nums[right+1]):
                            right -= 1
        return result