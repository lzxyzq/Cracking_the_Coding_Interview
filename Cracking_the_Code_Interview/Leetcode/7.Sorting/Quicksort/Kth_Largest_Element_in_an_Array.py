'''
@Author: your name
@Date: 2020-05-31 17:00:00
@LastEditTime: 2020-06-20 18:59:52
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Sorting/Quicksort/Kth_Largest_Element_in_an_Array.py
'''
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

''' 
Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
'''

# 堆排序，维护一个k大小的小根堆，将数组中的每个元素与堆顶元素进行比较，如果比堆顶元素大，则删除堆顶元素并添加该元素，如果比堆顶元素小，则什么也不做，继续下一个元素。时间复杂度O(nlogk)，空间复杂度O(k)。
# 利用快速排序中的partition思想，从数组中随机选择一个元素x，把数组划分为前后两部分sa和sb，sa中的元素小于x，sb中的元素大于或等于x。这时有两种情况：
# sa的元素个数小于k，则递归求解sb中的第k-|sa|大的元素
# sa的元素个数大于或等于k，则递归求解sa中的第k大的元素
# 时间复杂度O(n)，空间复杂度O(1)

# Method 1 
class Solution:
    def findKthLargest(self, nums, k) :
        return sorted(nums)[-k]
# Sort and return --> O(NlogN)

# Method 2 
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int):
        heap = []
        for num in nums:
            heapq.heappush(heap,num) # always be a min-heap with size of k, k largest candidates from now on
            if len(heap) > k :
                heapq.heappop(heap)
        return heapq.heappop(heap)

# Time: O(k+(N-k)*logk) = O(nlogk), O(k) for building a heap, insert one element takes logk, and insert n-k elements
# Space: O(k) to store the heap elements.

# Method 2
import heapq   
class Solution:
    def findKthLargest(self, nums: List[int], k: int) :
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)  # always be a min-heap with size of k, k largest candidates from now f
            else:
                if num > heap[0]:
                    heapq.heappushpop(heap, num)
        return heap[0]

# Method 2
import heapq   
class Solution:
    def findKthLargest(self, nums: List[int], k: int):
        heap = [num for num in nums]
        heapq.heapify(heap)
        for _ in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)

# Method 3 
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]  
            
            return store_index
        
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element
            
            # select a random pivot_index between 
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest 
        return select(0, len(nums) - 1, len(nums) - k)

# Time : 平均情况 O(N)，最坏情况 O(N^2)。
# Space : O(1)。