class Solution:
    def lengthoflis(self,nums):
        return self.helper(nums,float('-inf'),0)
    def helper(self,nums,prev,curpos):
        if curpos == len(nums):
            return 0 
        taken = 0
        if nums[curpos] > prev:
            taken = 1 + self.helper(nums,nums[curpos],curpos+1)
        nottaken = self.helper(nums,prev,curpos + 1)
        return max(taken,nottaken)

if __name__ == '__main__':
    print(Solution().lengthoflis([10,9,2,5,3,7,101,18]))

    
