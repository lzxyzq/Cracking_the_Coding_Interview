'''
@Author: your name
@Date: 2020-05-23 10:28:11
@LastEditTime: 2020-05-23 12:08:03
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Tree/303.Range_Sum_Query_Immutable.py
'''
# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

''' 
Example:
Given nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3 '''

# Solution: Prefix sum
# sums[i] = nums[0] + nums[1] + … + nums[i]

# sumRange(i, j) = sums[j] – sums[i – 1]

# Time complexity: pre-compute: O(n), query: O(1)

# Space complexity: O(n)
class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.sums_ = nums[:]
        if not nums:
            return 
        for i in range(1,len(nums)):
            self.sums_[i] += self.sums_[i - 1]

    def sumRange(self, i, j) :
        if (i == 0) :
            return self.sums_[j]
        return self.sums_[j] - self.sums_[i-1]
# ------------------------------------------------------------------------
if __name__ == '__main__':
    a = NumArray(nums= [5,18,13])
    print(a.sumRange(0,2))
    
        