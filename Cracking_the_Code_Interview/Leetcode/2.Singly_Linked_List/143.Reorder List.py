'''
@Author: your name
@Date: 2020-06-17 11:24:47
@LastEditTime: 2020-06-17 11:26:21
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Singly_Linked_List/143.Reorder List.py
'''
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You may not modify the values in the list's nodes, only nodes itself may be changed.

""" Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        a, b = self._splitList(head)
        b = self._reverseList(b)
        self._mergeLists(a, b)
        return a
    
    def _splitList(self,head):
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        slow.next = None
        return head, middle

# Reverses in place a list.
# @return Returns the head of the new reversed list
    def _reverseList(self,head):
        last = None
        currentNode = head
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = last
            last = currentNode
            currentNode = nextNode
        return last
    
# Merges in place two lists
# @return The newly merged list.
    def printList(self,node) : 
        while (node!=None):
            print(node.val,end=" ")
            node = node.next

    def _mergeLists(self,a, b):
        l1 = a 
        while (b):
            next = l1.next
            l1.next = b
            b = b.next
            l1.next.next = next 
            l1 = next 