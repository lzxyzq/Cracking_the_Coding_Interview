'''
@Author: your name
@Date: 2020-06-14 23:34:31
@LastEditTime: 2020-06-15 11:22:06
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Singly_Linked_List/83.Remove_Duplicates_from_Sorted_List.py
'''
# Given a sorted linked list, delete all duplicates such that each element appear only once.

''' Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''
class Solution:
    def deleteDuplicates(self, head):
        current  = head 
        while (current and current.next):
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head 

