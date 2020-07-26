'''
@Author: your name
@Date: 2020-07-10 14:03:41
@LastEditTime: 2020-07-10 14:28:54
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/3.String/344.Reverse_String.py
'''
# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.

''' 
Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"] 
'''

''' 
Does in-place mean constant space complexity?
No. By definition, an in-place algorithm is an algorithm which transforms input using no auxiliary data structure.\

The tricky part is that space is used by many actors, not only by data structures. The classical example is to use recursive function without any auxiliary data structures.

Is it in-place? Yes.

Is it constant space? No, because of recursion stack. 
'''


# Method 0

class Solution:
    def reverseString(self, s):
        s.reverse()
# in-place 

class Solution:
    def reverseString(self, s: List[str]) :
        s[:] = s[::-1]

# Note:
# s[:] = s[::-1] is required NOT s = s[::-1] because you have to edit the list inplace. 


# Method 1 
# Recursion, In-Place, O(N) Space

class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)


# Complexity Analysis
# Time complexity : N/2 swaps.
# Space complexity : O(N) to keep the recursion stack.

# Method 2 
# Two Pointers, Iteration O(1) Space

class Solution:
    def reverseString(self, s: List[str]) :
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0,len(s)-1
        while left < right:
            s[left] ,s[right] = s[right],s[left]
            left, right = left + 1 ,right - 1

# Method 3 
