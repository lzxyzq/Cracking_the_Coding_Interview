'''
@Author: your name
@Date: 2020-06-15 17:02:02
@LastEditTime: 2020-06-15 21:19:31
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Singly_Linked_List/19.Remove_Nth_Node_From_End_of_List.py
'''
# Given a linked list, remove the n-th node from the end of list and return its head.

''' 
Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = first = second =  ListNode(-1)
        dummy.next = head
        for i in range(n+1):
            first = first.next
        while(first):
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 1
        p = head
        while p.next:
            length +=1 
            p = p.next
        dummy = ListNode(-1)
        dummy.next = head
        
        length -= n
        first = dummy
        while (length > 0):
            length -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next