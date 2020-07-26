# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

""" 
Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6. 
"""

class Solution:
    def maxSubArray(self, nums: List[int]) :
        if max(nums) < 0:
            return max(nums)
        local_max,global_max = 0,0
        for num in nums:
            local_max = max(0, local_max + num)
            global_max = max(global_max,local_max)
        
        return global_max


# -------------------------------------------------------------------
A = [-2,1,-3,4,-1,2,1,-5,4]
def maxSum(A):
    start = end = Max = 0
    for i in range(len(A)):
        local_max = 0
        for j in range(i,len(A)):
            local_max += A[j]
            if local_max > Max:
                start = i
                end = j
                Max = local_max
    print("start:"+ str(start))
    print("end:"+ str(end))
    return Max
maxSum(A)

A = [-2,1,-3,4,-1,2,1,-5,4]
def maxSum2(A):
    start = end = Max = local_max = 0
    for i in range(len(A)):
        local_max += A[i]
        if local_max > Max:
            end = i
            Max = local_max

        if local_max < 0:
            local_max = 0
            if (i <= len(A) - 2 and A[i+1] > 0):
                start = i + 1
    print("start:" + str(start))
    print("end:" + str(end))
    return Max
maxSum2(A)

