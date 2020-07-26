'''
@Author: your name
@Date: 2020-06-15 21:33:47
@LastEditTime: 2020-06-16 00:39:41
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Singly_Linked_List/24.Swap_Nodes_in_Pairs.py
'''
# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes, only nodes itself may be changed.

''' Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
'''

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = prev = ListNode(-1)
        prev.next = head 
        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next
            c = prev.next.next.next
            prev.next = b
            prev.next.next = a
            prev.next.next.next = c
            prev = prev.next.next
        return dummy.next



