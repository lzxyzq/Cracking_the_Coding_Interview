# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
''' Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
class Solution:
    def combine(self, n, k):
        result = []
        nums = [i for i in range(1,n+1)]
        self.helper(nums,[],result,k)
        return result
    def helper(self,nums,path,result,k):
        if len(path) == k:
            result.append(path)
        for i in range(len(nums)):
            self.helper(nums[i+1:],path+[nums[i]],result,k)