# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

''' 
Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order. 
'''

# Method 1 
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_copy = sorted(nums)
        start = len(nums)
        end = 0
        for i in range(len(nums)):
            if nums_copy[i] != nums[i]:
                start = min(start,i)
                end = max(end,i)
        return end - start + 1 if end - start >= 0 else 0

# Time complexity : O(nlogn). Sorting takes nlogn time.
# Space complexity : O(n). We are making copy of original array.

# Method 2 (TLE)
# Better Brute Force
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = len(nums)
        end = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] < nums[i]:
                    start = min(start,i)
                    end = max(end,j)
        return end - start + 1 if end - start >= 0 else 0

# Time complexity : O(n2).Two nested loops are there.
# Space complexity : O(1). Constant space is used.

# Method 3 
# Using Stack
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = len(nums)
        end = 0
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                start = min(start,stack.pop())
            stack.append(i)
        stack.clear()
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]] < nums[i]:
                end = max(end,stack.pop())
            stack.append(i) 
        return end - start + 1 if end - start >= 0 else 0

# Method 4 
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
     
        if len(nums) == 1:
            return 0
        
        min_ = float("inf")
        max_ = float("-inf")
        flag = False 
        
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                flag = True
            if flag:
                min_ = min(min_,nums[i])
        flag = False
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > nums[i+1]:
                flag = True
            if flag:
                max_ = max(max_, nums[i])
   
        for l in range(len(nums)):
            if min_ < nums[l]:
                break
        
        for r in range(len(nums)-1,-1,-1):
            if max_ > nums[r]:
                break

        return r - l + 1 if r - l > 0 else 0

# Time complexity : O(n). Four O(n) loops are used.
# Space complexity : O(1). Constant space is used.
