'''
@Author: your name
@Date: 2020-06-14 23:31:33
@LastEditTime: 2020-06-14 23:31:34
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Singly_Linked_List/86.Partition_List.py
'''
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

''' Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int):
        temp1 = l1 = ListNode(0)
        temp2 = l2 = ListNode(0)
        while head:
            if head.val < x:
                temp1.next = ListNode(head.val)
                temp1 = temp1.next
            else:
                temp2.next = ListNode(head.val)
                temp2 = temp2.next
            head = head.next
        temp1.next = l2.next
        return l1.next