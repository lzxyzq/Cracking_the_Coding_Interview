# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

''' 
Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()" 
'''


# Method 1
# Brute Force

# Complexity Analysis
# Time complexity : O(n^3). 
# Generating every possible substring from a string of length n requires O(n^2)
# Checking validity of a string of length n requires O(n).
# Space complexity : O(n). A stack of depth n will be required for the longest substring.

# Method 2 
class Solution:
    def longestValidParentheses(self, s: str):
        maxnum = 0
        lens = len(s)
        dp = [0 for i in range(lens)]
        for i in range(1,lens):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2 
                elif i-dp[i-1] > 0 and s[i-dp[i-1]-1] == '(' :
                    dp[i] = dp[i-1] + (dp[i-dp[i-1]-2] if i-dp[i-1] >= 2 else 0) + 2 
                maxnum = max(maxnum,dp[i])
        return maxnum                   
                    

# Complexity Analysis

# Time complexity : O(n). Single traversal of string to fill dp array is done.

# Space complexity : O(n). dp array of size nn is used.  
            