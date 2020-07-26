'''
@Author: your name
@Date: 2020-06-03 00:36:23
@LastEditTime: 2020-06-03 00:45:26
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Array/169.Majority_Element.py
'''
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

''' Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

'''
# https://www.geeksforgeeks.org/majority-element/
from collections import Counter
class Solution:
    def majorityElement(self, nums):
        count = Counter(nums)
        m = len(nums) // 2
        for key, value in count.items():
            if value > m:
                return key
# ----------------------------------------------------------------------
# Using Moore’s Voting Algorithm

class Solution:
    def majorityElement(self, nums):
        cnt,index = 1,0
        for i in range(len(nums)):
            if nums[i] == nums[index]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    index = i
                    cnt = 1
        return nums[index]
