'''
@Author: your name
@Date: 2020-06-02 20:15:35
@LastEditTime: 2020-06-02 21:37:28
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Array/60.Permutation_Sequence.py
'''
# The set [1,2,3,...,n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Note:

# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.

''' Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
'''
# 分组 以len(nums)-1为一组 依次减k,看有几个K余几， 第一组为0开始
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''
        nums = [i for i in range(1,n+1)]
        for i in range(n-1,0,-1):
            base = math.factorial(i)
            current = 0
            while k > base:
                k -= base
                current += 1
            res += str(nums[current])
            nums.pop(current)
        res += str(nums[0])
        return res
#------------------------------------------------
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def fact(n):
            r = 1
            for i in range(2,n+1):
                r *= i
            return r
        
        nums = [str(i) for i in range(1,n+1)]
        s=''
        while(nums):
            div = fact(len(nums)-1)
            idx = 0
            while(k>div):
                idx += 1
                k -= div
                
            s += nums.pop(idx)
            
        return s