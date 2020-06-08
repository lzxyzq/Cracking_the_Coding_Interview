'''
@Author: your name
@Date: 2020-06-06 20:41:59
@LastEditTime: 2020-06-06 21:14:30
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Array/238.Product_of_Array_Except_Self.py
'''
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

''' Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer. 
'''

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums) :
        length = len(nums)
        L, R, answer = [0]*length, [0]*length, [0]*length
        
        L[0] = 1
        for i in range(1, length):
            L[i] = L[i-1] * nums[i-1]
        
        R[length-1] = 1
        for i in range(length - 2, -1 ,-1):
            R[i] = nums[i+1] * R[i + 1]
        
        for i in range(length):
            answer[i] = L[i] * R[i]
        return answer
            

# Complexity analysis

# Time complexity : O(N)O(N) where NN represents the number of elements in the input array. We use one iteration to construct the array LL, one to construct the array RR and one last to construct the answeranswer array using LL and RR.

# Space complexity : O(N)O(N) used up by the two intermediate arrays that we constructed to keep track of product of elements to the left and right.

# ---------------------------------------------------------------
class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        answer = [0]*length
        
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
       
        R = 1;
        for i in range(length-1,-1,-1):
            answer[i] = answer[i] * R 
            R*= nums[i]
            
        return answer

# Complexity analysis

# Time complexity : O(N)O(N) where N represents the number of elements in the input array. We use one iteration to construct the array LL, one to update the array answeranswer.

# Space complexity : O(1) since don't use any additional array for our computations. The problem statement mentions that using the answeranswer array doesn't add to the space complexity.