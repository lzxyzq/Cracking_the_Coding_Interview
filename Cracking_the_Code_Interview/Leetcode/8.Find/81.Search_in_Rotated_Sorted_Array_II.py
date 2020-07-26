# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

# You are given a target value to search. If found in the array return true, otherwise return false.

""" Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
"""


# Method 1 
class Solution:
    def search(self, nums: List[int], target: int):
        return target in nums


# Method 2

""" Analysis：
Allow duplicate elements，If A[left] <= A[mid], then the assumption that [left,mid] is an increasing sequence cannot be held, such as [1,3,1,1,1].

A[left] <= A[mid]：
    (1)if A[left] < A[mid]，[left,mid] must be an increasing sequence 
    (2)if A[left] == A[mid]  left++。
 """
# Four parts to find
 class Solution:
        def search(self, nums: List[int], target: int):
        lo = 0 
        hi = len(nums) - 1 
        while (lo <= hi):
            mid = lo + (hi - lo)//2
            if nums[mid] == target:
                return True 
            if nums[mid] == nums[hi]:
                hi -= 1 
            elif nums[mid] < nums[hi]:
                if target >= nums[mid] and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                if target >= nums[lo] and target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

                
                    
                    