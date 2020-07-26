# Given a non-empty array of integers, return the k most frequent elements.
''' 
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1] 
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        res = []
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1 
        for key, val in dict.items():
            if len(res) < k:
                heapq.heappush(res,[val,key])
            else:
                heapq.heappushpop(res,[val,key])
        return [y for x,y in res]


        