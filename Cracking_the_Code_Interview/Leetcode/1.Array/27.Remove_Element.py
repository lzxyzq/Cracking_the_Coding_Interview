'''
Author: your name
Date: 2020-06-02 10:05:22
LastEditTime: 2020-09-29 13:38:08
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /Cracking_the_Code_Interview/Leetcode/1.Array/27.Remove_Element.py
'''
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

'''
Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
'''

def removeElement(nums, val):
    i = 0 
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i+=1
    return nums

print(removeElement([1,2,3,4,4],4))