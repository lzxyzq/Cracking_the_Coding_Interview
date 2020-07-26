# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

# Follow up:
# Could you solve it in linear time?



''' 
Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 '''

# 单调递减双向队列 Monotonic Queue
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ln = len(nums)
        if ln == 0:
            return []
    
        queue = []
        for i in range(k):
            while queue and queue[-1][0] <= nums[i]:
                queue.pop()
            queue.append((nums[i], i))

        i = k
        result = [queue[0][0]]
        while i < ln:
            #remove the first element from the queue if it is outside the window
            if i - queue[0][1] >= k:
                queue.pop(0)

            # also remove any elements that are less than the current num
            # as long as the current num is in the boundary I don't care about any other number
            # if this is the max, then be it.
            while queue and queue[-1][0] <= nums[i]:
                queue.pop()
            queue.append((nums[i], i))

            result.append(queue[0][0])
            i += 1

        return result


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        que = collections.deque() # [[i, num]]
        res = []
        for i, num in enumerate(nums):
            if que and i - que[0][0] >= k:
                que.popleft()
            while que and que[-1][1] <= num:
                que.pop()
            que.append([i, num])
            if i >= k - 1:
                res.append(que[0][1])
        return res
