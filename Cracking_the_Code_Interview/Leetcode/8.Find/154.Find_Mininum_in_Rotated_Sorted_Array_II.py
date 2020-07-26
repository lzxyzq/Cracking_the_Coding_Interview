'''
@Author: your name
@Date: 2020-06-22 00:49:26
@LastEditTime: 2020-06-22 02:06:23
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Find/154.Find_Mininum_in_Rotated_Sorted_Array_II.py
'''
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# The array may contain duplicates.

""" Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
"""

""" 判断“断层”在左边还是右边。
1.A[mid] < A[right]，则区间[mid,right]一定递增，断层一定在左边
2.A[mid] > A[right]，则区间[left,mid]一定递增，断层一定在右边
3.若A[mid] == A[right] 确定不了，这个时候，断层既可能在左边，也可能在右边，所以我们不能扔掉一半，不过这时，我们可以--right扔掉一个 
"""
class Solution:
    def findMin(self, nums: List[int]):
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if nums[mid] < nums[hi]:
                hi = mid - 1 
            elif nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi -= 1
        return nums[lo]

# Time:O(logn) Worst:O(n)
# Space:O(1)