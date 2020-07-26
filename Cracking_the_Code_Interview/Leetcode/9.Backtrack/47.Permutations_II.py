# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
''' 
Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
] 
'''
class Solution:
    def permuteUnique(self, nums) :
        result = []
        # sort the list to keep same values adjacent to each other 
        nums.sort()
        # call helper function to recursively find all permutations
        self.helper(nums,[],result)
        return result
    def helper(self,nums,path,result):
        # if there's no path, we found a result, append and return
        if not nums:
            result.append(path)
        # iterate over the list
        for i in range(len(nums)):
            # if list is identified to be similar to pevious item, 
            # skip calling helper
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # append current element to result, 
            # and continue finding permutations for other members
            self.helper(nums[:i]+nums[i+1:],path + [nums[i]],result)

        