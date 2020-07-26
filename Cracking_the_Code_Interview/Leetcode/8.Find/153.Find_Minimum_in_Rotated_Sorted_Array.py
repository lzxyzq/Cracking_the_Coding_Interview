'''
@Author: your name
@Date: 2020-06-21 20:44:56
@LastEditTime: 2020-06-22 14:23:53
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Find/153.Find_Minimum_in_Rotated_Sorted_Array.py
'''
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# Find the minimum element.
# You may assume no duplicate exists in the array.

""" Example 1:
Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""
# Method 1 
class Solution:
    def findMin(self, nums: List[int]):
         return self.helper(nums,0,len(nums)-1)
    
    def helper(self,nums,low,high):
        # Only one or two elements
        if low + 1 >= high:
            return min(nums[low],nums[high])
        # Sorted
        if nums[low] < nums[high]:
            return nums[low]
        
        mid = low + (high - low)//2
        return min(self.helper(nums,low,mid-1),self.helper(nums,mid,high))


# Method 2 

""" Algorithm
1.Find the mid element of the array.

2.If mid element > first element of array this means that we need to look for the inflection point on the right of mid.

3.If mid element < first element of array this that we need to look for the inflection point on the left of mid. 

4 We stop our search when we find the inflection point, when either of the two conditions is satisfied:
    (1)nums[mid] > nums[mid + 1] Hence, mid+1 is the smallest.
    (2)nums[mid - 1] > nums[mid] Hence, mid is the smallest.
"""

class Solution:
    def findMin(self, nums: List[int]):
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]
        lo = 0
        hi = len(nums) - 1
        
        # Sorted
        if nums[hi] > nums[lo]:
            return nums[0]
        
        # Binary search way
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if nums[mid] > nums[mid + 1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                lo = mid + 1
            else:
                right = mid - 1 