'''
@Author: your name
@Date: 2020-06-01 02:02:59
@LastEditTime: 2020-06-02 00:18:15
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Array/15.3Sum.py
'''
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:
# The solution set must not contain duplicate triplets.

''' Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
         # check empty, all negative, all positive
        if not nums or nums[0] > 0 or nums[len(nums)-1] < 0:
            return []
        for k in range(len(nums)-2):
            if nums[k] > 0:
                break
            # skip duplicate value
            if k > 0 and nums[k] == nums[k-1]:
                continue 
            target = 0 - nums[k]
            i = k+1 
            j = len(nums) -1
            while i < j:
                if nums[i] + nums[j] == target:
                    temp = []
                    temp.append(nums[k])
                    temp.append(nums[i])
                    temp.append(nums[j])
                    res.append(temp)
                    # skip duplicate value
                    while(i < j and nums[i] == nums[i+1]):
                        i = i + 1
                    while(i < j and nums[j] == nums[j-1]):
                        j = j - 1
                    i = i + 1
                    j = j - 1 
                elif nums[i] + nums[j] < target:
                    i = i + 1
                else:
                    j = j - 1
        return res          


seen = {}
seen['1'] = [(1,2)]
for i in seen['1']:
    print(i[0])

