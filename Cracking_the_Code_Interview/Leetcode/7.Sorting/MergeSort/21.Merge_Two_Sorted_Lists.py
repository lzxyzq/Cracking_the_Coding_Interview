'''
@Author: your name
@Date: 2020-06-18 22:36:49
@LastEditTime: 2020-06-19 07:44:04
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Sorting/MergeSort/21.Merge_Two_Sorted_Arrays.py
'''
# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

""" Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(float("-inf"))  # a dummy node
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:  # sorted
                cur.next = l1
                l1 = l1.next  # go ahead
            else:
                cur.next = l2
                l2 = l2.next  # go ahead
            cur = cur.next  # go ahead
        # when one of them is None, cur should point at the remainder since the linked lists are sorted
        cur.next = l1 if l1 else l2
        return dummy.next

# Iteratively with two pointers
# Time: O(n+m). Because exactly one of l1 and l2 is incremented on each loop iteration, the while loop runs for a number of iterations equal to the sum of the lengths (m + n) of the two lists. All other work is constant, so the overall complexity is linear.
# Space: O(1). only allocates a few pointers, so it has a constant overall memory footprint.