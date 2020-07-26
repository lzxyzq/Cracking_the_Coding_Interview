# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

""" Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2] 
"""
# Method 1: Two-pass algorithm using counting sort.
# Because there are only three numbers, the simple method is to count and sort. The first traversal counts the number of occurrences of these three numbers, and the second traversal modifies the original list according to the number of three numbers.
from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = [2,2,1,1,0,0]
        count = Counter(nums)
        for i in range(len(nums)):
            if i < count[0]:
                nums[i] = 0
            elif i < count[0] + count[1]:
                nums[i] = 1
            else:
                nums[i] = 2
# Time: O(N), N is the length of the input array
# Space: O(N), save count of three color and reformed array

# Method 2: One-pass algorithm
class Solution:
    def sortColors(self, nums: List[int]) :
        """
        Do not return anything, modify nums in-place instead.
        """
        L, R, i = 0, len(nums) - 1, 0
        while i <= R:
            if nums[i] == 0: 
                nums[L], nums[i], L, i = 0, nums[L], L + 1, i + 1
            elif nums[i] == 2: 
                nums[R], nums[i], R = 2, nums[R], R - 1
            else: i += 1


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # (1) initialize rightmost boundary of zeros and leftmost boundary of twos 
        p0 = 0                 # for all idx < p0: nums[idx < p0] = 0
        curr = 0               # curr is index of element under consideration
        p2 = len(nums) - 1     # for all idx > p2: nums[idx > p2] = 2

        # (2) traverse the array
        while curr <= p2:
            # (2.1) If nums[curr] = 0, swap curr and p0 elements and move both pointers to right
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            
            # (2.2) If nums[curr] = 2, swap curr and p2 elements, and Move pointer p2 to left
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
                
            # (2.3) If nums[curr] = 1 : move pointer curr to the right.
            else:
                curr += 1


# Time: O(N) since it's one pass along the array of length N.
# Space: O(1) since it's a constant space solution.