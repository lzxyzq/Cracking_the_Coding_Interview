'''
@Author: your name
@Date: 2020-05-31 17:00:00
@LastEditTime: 2020-05-31 18:46:08
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Sorting/Quicksort/Kth_Largest_Element_in_an_Array.py
'''
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

''' 
Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
'''

class Solution:
    def findKthLargest(self, nums, k) :
        return sorted(nums)[-k]
