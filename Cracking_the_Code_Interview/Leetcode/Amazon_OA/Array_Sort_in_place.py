'''
Author: your name
Date: 2020-09-29 14:53:03
LastEditTime: 2020-10-01 01:12:46
LastEditors: your name
Description: In User Settings Edit
FilePath: /Cracking_the_Code_Interview/Leetcode/Amazon_OA/Array_Sort_in_place.py
'''
# 给个排序好的integer数组[1,1,1,2,2,3,4], 输出：[1,2,3,4,1,1,2]; 就是前面排序好的， 最后三个数字1，1，2不需要排序好。


def array_sort(nums) :
    """
    Do not return anything, modify nums in-place instead.
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != nums[slow]:
            nums[slow+1],nums[fast] = nums[fast],nums[slow+1]
            slow += 1
    return nums

print(array_sort([0,0,1,1,2,2,3,3]))