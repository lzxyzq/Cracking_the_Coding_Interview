# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.


class Solution:
    def subsetsWithDup(self, nums) :
            result = []
            nums.sort()
            self.helper(nums,0,[],result)
            return result
    def helper(self,nums,index,path,result):
        result.append(path)
        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.helper(nums,i+1,path+[nums[i]],result)

if __name__ == '__main__':
    Solution().subsetsWithDup([1,2,2])
    