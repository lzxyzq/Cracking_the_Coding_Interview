'''
@Author: your name
@Date: 2020-06-19 15:51:54
@LastEditTime: 2020-06-19 21:42:12
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Sorting/MergeSort/148.Sort_List.py
'''
# Sort a linked list in O(n log n) time using constant space complexity.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):
        if not head:
            return None
        if not head.next:
            return head

        pre = None
        slow = head 
        fast = head
        while fast and fast.next:
            pre = slow 
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        
        left_merge = self.sortList(head)
        right_merge = self.sortList(slow)
        
        new_head = dummy =  ListNode()
        
        while left_merge and right_merge:
            if left_merge.val <= right_merge.val:
                new_head.next = left_merge
                left_merge = left_merge.next
            else:
                new_head.next = right_merge
                right_merge = right_merge.next
            new_head = new_head.next
        if left_merge:
            new_head.next = left_merge
            
        if right_merge:
            new_head.next = right_merge
        
        return dummy.next
              
            
         
         