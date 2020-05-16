# Write a method to compute all permutations of a string whose characters are not necessarily unique.The list of permutations should not have duplicates.

#47 Permutations II
class Solution:
    def permuteUnique(self, nums):
        self.result = []
        self.length = len(nums)
        self.helper(nums,[],)
        return self.result
    
    def helper(self,nums,tmp):
        if len(tmp) == self.length and tmp not in self.result:
            self.result.append(tmp)
        for i in range(len(nums)):
            self.helper(nums[0:i]+nums[i+1:],tmp+[nums[i]])
#------------------------------------------------------------------------------------------------------------------------------
# In this situations where the string has many duplicates,this algorithm will run a lot faster than the earlier algorithm.
    
    
#------------------------------------------------------------------------------------
    def permuteUnique2(self, nums) :
        # if there's no nums provided
        if not nums:
            return []
        # results candidate
        results = []
        # helper function to find all permutations
        def helper2(path, result):
            # if there's no path, we found a result, append and return
            if not path:
                results.append(result)
            # iterate over the list
            for it in range (len (path)):
                # if list is identified to be similar to pevious item, 
                # skip calling helper
                if it > 0 and path[it-1] == path[it]:
                    continue
                # append current element to result, 
                # and continue finding permutations for other members
                helper2(path[0:it] + path[it+1:], result + [path[it]])
        # sort the list to keep same values adjacent to each other 
        nums.sort ()
        # call helper function to recursively find all permutations
        helper2(nums, [])
        return results

if __name__ == '__main__':
    # print(Solution().permuteUnique([1,1,2]))
    print(Solution().permuteUnique2([1,1,2]))
    