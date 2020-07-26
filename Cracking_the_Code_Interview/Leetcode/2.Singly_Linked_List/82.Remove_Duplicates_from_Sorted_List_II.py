'''
@Author: your name
@Date: 2020-06-15 12:22:08
@LastEditTime: 2020-06-15 12:26:12
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Singly_Linked_List/82.Remove_Duplicates_from_Sorted_List.py
'''
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# Return the linked list sorted as well.

''' Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = save_head = ListNode(-1)
        save_head.next = head
        duplicate = False
        while head and head.next:
            while head and head.next and head.val == head.next.val:
                head = head.next 
                duplicate = True
            if duplicate:
                pre.next = head.next
                duplicate = False
            else:
                pre = head
            head = head.next
        return save_head.next
