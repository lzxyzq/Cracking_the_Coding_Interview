'''
@Author: your name
@Date: 2020-06-07 20:49:02
@LastEditTime: 2020-06-07 22:03:42
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Array/334.Increasing_Triplet_Subsequence.py
'''
# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
# Formally the function should:
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

# Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.
''' Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false 
'''

class Solution:
    def increasingTriplet(self, nums):
        return self._increasingTriplet(nums,3)
    def _increasingTriplet(self,nums,k):
        small_arr = [float(inf)] * (k -1)
        for num in nums:
            for i in range(k-1):
                if num <= small_arr[i]:
                    small_arr[i] = num
                    break
            if num > small_arr[-1]:
                return True
        return False
