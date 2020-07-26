# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

""" 
Example 1:

Input:nums = [1,1,1], k = 2
Output: 2 
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) :
        dic = {0:1}
        count = sum = 0 
        for num in nums:
            sum += num
            if sum - k in dic:
                count+=dic[sum-k]
            dic[sum] = dic.get(sum,0) + 1 
        return count
            
# Complexity Analysis

# Time complexity : O(n). The entire numsnums array is traversed only once.
# Space complexity : O(n). Hashmap mapmap can contain upto nn distinct entries in the worst case.


