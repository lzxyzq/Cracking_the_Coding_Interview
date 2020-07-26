# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

''' 
Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6] 
'''
# Method 1 
# 数组位置和值相差1
# 遍历数组将出现的数字其本应所在的位置的数子乘-1,为正的数表示其位置的数缺少。

class Solution:
    def findDisappearedNumbers(self, nums: List[int]):
        if not nums:
            return None
        res = []
        for i in range(len(nums)):
            val = abs(nums[i])-1
            nums[val] = abs(nums[val]) * (-1)
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res

# Method 2 
class Solution:
    def findDisappearedNumbers(self, nums: List[int]):
        return list((set(range(1,len(nums)+1))) - (set(nums)))
        
# Method 3
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in N]
        