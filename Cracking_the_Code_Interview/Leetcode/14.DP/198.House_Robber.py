# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

''' 
Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''

# Method 1 
# 设状态 f[i] 为到位置i时能抢到的金钱最大和，那么状态转移方程如下：
# f[i]=max(f[i-1], f[i-2] + nums[i])
# 其含义是，如果不选择i，则抢到的钱是f[i-1]，如果选择i，则能抢到的钱是f[i-2] + nums[i]。

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2] + nums[i])
        return dp[-1]

# Method 2 
# 在状态转移方程中，我们可以发现 f[i]仅仅依赖前两项，因此用两个整数变量即可代替一位数组，将空间复杂度降为O(1)。
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        even = nums[0]
        odd = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            if (i % 2 == 0):
                even = max(even + nums[i], odd)
            else:
                odd = max(odd + nums[i], even)
        return max(even, odd);