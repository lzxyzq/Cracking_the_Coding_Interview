# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

''' 
Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
] '''

# Method 1
# Iteratively
class Solution:
    def subsets(self, nums):
        res = [[]]
        for num in nums:
            res += [item + [num] for item in res]
        return res


# Method 2
# Backtracking
class Solution2:
    def subsets(self, nums):
        res = []
        self.dfs(nums,0,[],res)
        return res
        
    def dfs(self,nums,index,path,res):
        res.append(path)
        for i in range(index,len(nums)):
            self.dfs(nums,i+1,path+[nums[i]],res)
    
if __name__ == '__main__':
    print(Solution2().subsets([1,2,3]))
    