# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
# Find out how many ways to assign symbols to make sum of integers equal to target S.

''' 
Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3. 
'''
# Method 1 Brute Force

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.count = 0
        self.calculate(nums,0,0,S)
        return self.count
    def calculate(self,nums,i,total,S):
        
        if i == len(nums):
            if total == S:
                self.count += 1
        else:
            self.calculate(nums,i+1,total+nums[i],S)
            self.calculate(nums,i+1,total-nums[i],S)

# Time complexity : O(2^n). Size of recursion tree will be 2^n.n refers to the size of nums array.
# Space complexity : O(n). The depth of the recursion tree can go upto n.


# Method 2
# Recursion with Memoization
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n , memo, p = len(nums), {}, 0
        
        def f(p,S, memo, nums):
            
            if((p,S) in memo): 
                return memo[(p,S)]
            if(p == n and S == 0):return 1            
            if(p == n and S != 0): return 0
            
            pos =  f(p + 1,S - nums[p], memo, nums)          
            neg =  f(p + 1, S + nums[p], memo, nums)            
            memo[(p,S)] = pos + neg
            
            return memo[(p,S)]
        
        return f(p,S, memo, nums)