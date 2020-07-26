# The set [1,2,3,...,n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
    # "123"
    # "132"
    # "213"
    # "231"
    # "312"
    # "321"
# Given n and k, return the kth permutation sequence.
''' 
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314" 
'''
# Backtracking
class Solution:
    def getPermutation(self, n: int, k: int):
        result = []
        nums = [i for i in range(1,n+1)]
        self.helper(nums,'',result,n)
        return result[k-1]
    def helper(self,nums,path,result,n):
        if len(path) == n:
            result.append(path)
        # if not nums:
        #     result.append(path)
        for i in range(len(nums)):
            self.helper(nums[:i] + nums[i+1:],path+str(nums[i]),result,n)

# Iterative 
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ''
        nums = [i for i in range(1,n+1)]
        for i in range(n-1,0,-1):
            base = math.factorial(i) # Num of each group
            current = 0  # Group 
            while k > base:
                k -= base
                current += 1
            res += str(nums[current])
            nums.pop(current)
        res += str(nums[0])
        return res
        
        

