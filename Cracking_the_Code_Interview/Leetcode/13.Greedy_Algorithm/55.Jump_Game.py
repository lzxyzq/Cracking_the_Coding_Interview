# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

""" 
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index. 
"""
# Here you can use dynamic programming to solve, maintain a one-dimensional array dp, where dp[i] represents the remaining jump force when reaching the i position, if the jump force is negative when reaching a certain position, it means that the position cannot be reached. The next difficulty is to deduce the state transition equation. Think about it. What does the remaining jump force at the current position have to do with it? In fact, it is the remaining jump force (dp value) of the previous position and the new jump force (nums) of the previous position. The value in the array) is relevant. The new jump force here is the number of each position in the original array, because it represents the farest position that can be reached starting from the current position. Therefore, the larger of the remaining jump force at the current position (dp value) and the new jump force at the current position determines the farest distance that can be reached at present, and the remaining jump force (dp value) at the next position is equal to the current This larger value minus 1, because it takes a jump force to reach the next position, so there is a state transition equation: dp[i] = max(dp[i-1], nums[i-1])-1 , If the value of the dp array is negative at a certain moment, indicating that the current position cannot be reached, then directly return false, and finally return true after the end of the loop.

# Method 1 
# DP 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1],nums[i-1]) - 1  
            if dp[i] < 0:
                return False
        return True

# Time: O(n)
# Space O(1)
 
            
# In fact, the best solution to this problem is not DP, but Greedy Algorithm, because here is not very concerned about the remaining steps at each position, but only want to know whether it can reach the end.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goodIndex = n-1
        for i in range(n-2,-1,-1):
            if nums[i] + i >= goodIndex:
                goodIndex = i
        return goodIndex == 0
        
      