# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
# The same repeated number may be chosen from candidates unlimited number of times.
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
""" 
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

# sorting and pruning more
class Solution:
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()
        self.helper(candidates,[],result,target)
        return result
    def helper(self,candidates,path,result,target):
        if target == 0:
            result.append(path)
        for i in range(len(candidates)):
            residue = target - candidates[i]
            if residue < 0:                   
                break
            self.helper(candidates[i:],path+[candidates[i]],result,residue)
        