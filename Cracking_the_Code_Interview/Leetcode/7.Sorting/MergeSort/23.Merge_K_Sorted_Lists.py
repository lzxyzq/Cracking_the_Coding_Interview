'''
@Author: your name
@Date: 2020-06-19 10:08:46
@LastEditTime: 2020-06-19 16:04:18
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Sorting/MergeSort/23.Merge_K_Sorted_Lists.py
'''
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

""" Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Method 1 Brute Force
class Solution:
    def mergeKLists(self, lists) :
        nodes = []
        head = cur = ListNode()
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next 
        for x in sorted(nodes):
            cur.next = ListNode(x)
            cur = cur.next
        return head.next

# Complexity Analysis

# Time complexity : O(NlogN) where N is the total number of nodes.
#     Collecting all the values costs O(N) time.
#     A stable sorting algorithm costs O(NlogN) time.
#     Iterating for creating the linked list costs O(N) time.
# Space complexity : O(N).
#     Sorting cost O(N) space (depends on the algorithm you choose).
#     Creating a new linked list costs O(N) space.

# Method2 Min Heap

from heapq import heappop, heappush
class Solution:
    def mergeKLists(self, lists):
        values, head, pointer = [], None, None
        
        for l in lists:
            while l:
                heappush(values, l.val)
                l = l.next
        
        while values:
            if head == None:
                head = ListNode(heappop(values))
                pointer = head
            else:
                pointer.next = ListNode(heappop(values))
                pointer = pointer.next
        
        return head
# Time complexity : O(NlogN)

# Sort
class Solution:
    def mergeKLists(self, lists) :
        values, head, pointer = [], None, None
        
        for l in lists:
            while l:
                values.append(l.val)
                l = l.next
                
        values.sort()
        
        while values:
            if head == None:
                head = ListNode(values.pop(0))
                pointer = head
            else:
                pointer.next = ListNode(values.pop(0))
                pointer = pointer.next
        
        return head

# Time complexity : O(NlogN)

# Method 3 Optimize Approach 2 by min heap / Priority Queue

from heapq import heappop, heappush
class Solution:
    def mergeKLists(self, lists):
        # (1) initialze a dummy node and current node and a heap
        heap = []
        dummy = ListNode(0)
        curr = dummy
        
        # (2) traverse all lists and put 1st number of k lists into heap (heap.size = k)
        for node in lists:
            if node:
                heappush(heap, (node.val, node))  #tuple 
                
        # (3) do some operations with heap
        while heap:
            # (3.1) connect current node with the node on the top of heap
            value, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            # (3.2) push the element that is next to the node you just removed into heap
            if curr.next:
                heapq.heappush(heap, (curr.next.val, curr.next))
                
        # (4) return the new linked list after dummu node
        return dummy.next
    
# Time: O(NKlogk) where k is the number of linked lists. N nodes in the final linked list.
# Space: O(N) for a new linked list. O(k) for heap

# python 3 heappush: TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'

# 出现原因：

# @cbmbbz In the event that two or more of the lists have the same val, this code will error out since the queue module will compare the second element in the priority queue which is a ListNode object (and this is not a comparable type).

 

# To solve for this issue, I have stored (node.val, list_idx, node) to account for this edge case.

from queue import PriorityQueue
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        k = len(lists)
        q = PriorityQueue(maxsize=k)
        dummy = ListNode(None)
        curr = dummy
        for list_idx, node in enumerate(lists):
            if node: q.put((node.val, list_idx, node))
        while q.qsize() > 0:
            poped = q.get()
            curr.next, list_idx = poped[2], poped[1]
            curr = curr.next
            if curr.next: q.put((curr.next.val, list_idx, curr.next))
        return dummy.next

# Complexity Analysis
# Time complexity : O(Nlogk) where k is the number of linked lists.
#     The comparison cost will be reduced to O(logk) for every pop and insertion to priority queue. But finding the node with the smallest value just costs O(1) time.
#     There are N nodes in the final linked list.
# Space complexity :
#     O(n) Creating a new linked list costs O(n) space.
#     O(k) The code above present applies in-place method which cost O(1) space. And the priority queue (often implemented with heaps) costs O(k) space (it's far less than NN in most situations).
