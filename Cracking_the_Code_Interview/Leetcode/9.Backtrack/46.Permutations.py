# Given a collection of distinct integers, return all possible permutations.
''' 
Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
] 
'''

# 选择列表（遍历每个元素）,路径添加元素,当选择列表为空时，添加至结果。

class Solution:
    def permute(self, nums):
        result = []
        self.helper(nums,[],result)
        return result
    def helper(self,nums,path,result):
        if not nums:
            result.append(path)
        for i in range(len(nums)):
            self.helper(nums[:i] + nums[i+1:],path + [nums[i]],result)
    
    