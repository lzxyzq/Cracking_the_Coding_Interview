'''
@Author: your name
@Date: 2020-06-03 00:56:30
@LastEditTime: 2020-06-03 13:05:04
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Array/189.Rotate_Array.py
'''
# Given an array, rotate the array to the right by k steps, where k is non-negative.
# Follow up:

# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# 最简单的方法，开一个k长的数组，先把右边k个元素存入这个临时数组，然后把数组中的前n-k右移k位，再把临时数组的k个元素存入到原始数组左边。时间复杂度O(n)，空间复杂度O(k)。
# 第二个简单的方法，先实现一个函数，把数组右移一位，调用这个函数k次即可。时间复杂度O(n*k)，空间复杂度O(1)。
# 第三个方法，先将数组分为两段，前n-k个为一段，后k个元素作为第二段，将第一段reverse, 第二段 reverse, 然后将整个数组reverse, 这样经过三轮reverse，就完成了循环右移。时间复杂度O(n)，空间复杂度O(1)。

# Brute Force
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]

# --------------------------------------------------------------
# 时间复杂度O(n)，空间复杂度O(1)。
# K可能大于数组长度，取余
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)  
        def reverse(begin,end):
            left = begin
            right = end - 1 
            while(left < right):
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right -= 1
        reverse(0,len(nums)-k)
        reverse(len(nums)-k,len(nums))
        reverse(0,len(nums))       
        