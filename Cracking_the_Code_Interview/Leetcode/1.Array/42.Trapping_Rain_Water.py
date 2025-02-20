'''
@Author: your name
@Date: 2020-06-02 22:01:07
@LastEditTime: 2020-06-02 22:04:31
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Array/42.Trapping_Rain_Water.py
'''
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

''' Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

class Solution:
    def trap(self, height):
        left = 0 
        right = len(height) - 1 
        ans = 0
        left_max = 0
        right_max = 0
        while(left < right):
            if height[left] < height[right]:
                if(height[left] >= left_max):
                    left_max = height[left]
                    left += 1   
                else:
                    ans += (left_max - height[left])
                    left += 1   
            else:
                if(height[right] >= right_max):
                    right_max = height[right]
                    right -= 1
                else:
                    ans += (right_max - height[right])
                    right -= 1
        return ans