# Given a sorted array of integers, find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].
# For example, Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].

# Method 1: linear scan
class Solution:
    def searchRange(self, nums, target):
        # find the index of the leftmost target. if it does not appear, return [-1, -1] early.
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        # find the index of the rightmost target (by reverse iteration). it is guaranteed to appear.
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]

# Time: O(n)
# Space: O(1)

# Method 2 

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        find_at = self.get_target_index(nums,0,len(nums)-1,target)
        
        if find_at is None:
            return [-1,-1]
        l = find_at 
        r = find_at 
        while(l > 0):
            if(nums[l-1] == target):
                l -= 1
            else:
                break
        while(r<len(nums)-1):
            if(nums[r+1] == target):
                r += 1
            else:
                break
        
        return [l,r]
    
    def get_target_index(self,nums,l,r,target):
        
        if r < l: 
            return None
        mid = int((r + l) / 2)
        num_mid = nums[mid]
        if num_mid == target: 
            return mid
        if num_mid < target:
            return self.get_target_index(nums, mid+1, r, target)
        if num_mid > target:
            return self.get_target_index(nums, l, mid-1, target)

#Method 3
class Solution:
    
    def first(self, arr, low, high, x, n) : 
        if(high >= low) : 
            mid = low + (high - low) // 2
            if( ( mid == 0 or x > arr[mid - 1]) and arr[mid] == x) : 
                return mid 
            elif(x > arr[mid]) : 
                return self.first(arr, (mid + 1), high, x, n) 
            else : 
                return self.first(arr, low, (mid - 1), x, n) 

        return -1
        
    def last(self,arr, low, high, x, n) : 
        if (high >= low) : 
            mid = low + (high - low) // 2
            if (( mid == n - 1 or x < arr[mid + 1]) and arr[mid] == x) : 
                return mid 
            elif (x < arr[mid]) : 
                return self.last(arr, low, (mid - 1), x, n) 
            else : 
                return self.last(arr, (mid + 1), high, x, n) 

        return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        left_index = self.first(nums, 0, n - 1, target, n)
        right_index = self.last(nums, 0, n - 1, target, n)
        return [left_index,right_index]
