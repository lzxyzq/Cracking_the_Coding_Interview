'''
@Author: your name
@Date: 2020-06-18 17:13:53
@LastEditTime: 2020-06-20 18:32:04
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Sorting/InsertSort/147.Insertion_Sort_List.py
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Method: two pointers
class Solution:
    def insertionSortList(self, head: ListNode):
        dummy = ListNode(0)      # pre is the sorted part when see a new node, start from dummy
        cur = head               # cur is the unsorted part
        
        while cur :
            pre = dummy
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
                
            temp = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = temp
        
        return dummy.next
    
# Time: O(n^2)
# Space: O(1)