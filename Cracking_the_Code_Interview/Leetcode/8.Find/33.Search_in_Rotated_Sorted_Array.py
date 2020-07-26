# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

""" Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

# If A[left] <= A[mid], then [left,mid] must be a monotonically increasing sequence.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1 
        while(lo<=hi):
            mid = lo + (hi - lo)//2 
            if (nums[mid] == target):
                return mid
            if nums[mid] >= nums[lo]: # left part is sorted 
                if nums[lo] <= target and nums[mid] >= target: # target is in the left part 
                    hi = mid - 1
                else:
                    lo = mid + 1 
            else:            # right part is sorted 
                if nums[mid] <= target and target <= nums[hi]: # target is in the right part 
                    lo = mid + 1
                else:
                    hi = mid - 1 
        return -1  
                

