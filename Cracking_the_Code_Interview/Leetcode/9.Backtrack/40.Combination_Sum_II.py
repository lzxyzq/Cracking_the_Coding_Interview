# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# Each number in candidates may only be used once in the combination.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

""" Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
] 
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort() 
        self.helper(candidates,[],result,target)
        return result
    def helper(self,candidates,path,result,target):
        if target == 0 :
            result.append(path)
        for i in range(len(candidates)):
            residue = target - candidates[i]
            if i > 0 and candidates[i] == candidates[i-1]:  # Skip duplicate values
                continue
            if residue < 0:   # pruning (given sorted) 
                break
            self.helper(candidates[i+1:],path+[candidates[i]],result,residue)