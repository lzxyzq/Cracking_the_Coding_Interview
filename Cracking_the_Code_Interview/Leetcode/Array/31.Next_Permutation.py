'''
@Author: your name
@Date: 2020-06-02 10:35:27
@LastEditTime: 2020-06-02 17:37:31
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Array/31.Next_Permutation.py
'''
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place and use only constant extra memory.
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2 
        while (i >= 0 and nums[i + 1 ] <= nums[i]):
            i-=1
        if(i >= 0):
            j = len(nums) - 1
            while(j >= 0 and nums[j] <= nums[i]):
                j-=1
            self.swap(nums,i,j)
        self.reverse(nums,i+1)
    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    
    def reverse(self,nums,start):
        i = start 
        j = len(nums) - 1
        while(i < j):
            self.swap(nums,i,j)
            i+=1
            j-=1