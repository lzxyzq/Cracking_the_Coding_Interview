'''
@Author: your name
@Date: 2020-05-31 21:12:01
@LastEditTime: 2020-05-31 21:13:10
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Array/83.Remove_Duplicates_from_Sorted_List.py
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
        current = head
        while current and current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head