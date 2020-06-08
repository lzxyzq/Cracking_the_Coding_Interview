'''
@Author: your name
@Date: 2020-06-02 22:17:00
@LastEditTime: 2020-06-02 22:22:10
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Array/70.Climbing Stairs.py
'''
# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

''' Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        
        prev,current = 0,1
        for i in range(n):
            prev,current = current, prev + current
        return current

