'''
@Author: your name
@Date: 2020-07-11 12:13:37
@LastEditTime: 2020-07-11 12:28:28
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Amazon_OA/347.Top_K_Frequent_Element.py
'''
# Given a non-empty array of integers, return the k most frequent elements.

''' 
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1] 
'''
import heapq
def topFrequent(nums,k):
    dict = {}
    res = []
    for num in nums:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
    for key,val in dict.items():
        if len(res) < k:
            heapq.heappush(res,[val,key])
        else:
            heapq.heappushpop(res,[val,key])
    return [key for val,key in res]

if __name__ == '__main__':
    print(topFrequent([1,1,1,2,2,3], k = 2))
    