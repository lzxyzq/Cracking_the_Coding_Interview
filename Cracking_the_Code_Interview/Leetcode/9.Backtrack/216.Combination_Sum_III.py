# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
# Note:

# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.

""" 
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]] 
"""
class Solution:
    def combinationSum3(self, k: int, n: int):
        result = []
        nums = [i for i in range(1,10)]
        self.helper(nums,[],result,k,n)
        return result
    def helper(self,nums,path,result,k,target):
        if len(path) == k and target == 0:
            result.append(path)
        # if len(path) > k:
        #     return
        for i in range(len(nums)):
            residue = target - nums[i] 
            if residue < 0:
                break
            self.helper(nums[i+1:],path+[nums[i]],result,k,residue)