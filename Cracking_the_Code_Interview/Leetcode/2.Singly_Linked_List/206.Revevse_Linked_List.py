'''
@Author: your name
@Date: 2020-06-14 09:37:18
@LastEditTime: 2020-06-14 10:13:58
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Singly_Linked_List/Revevse_Linked_List.py
'''
# Reverse a singly linked list.
''' Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''
# Approach #1 (Iterative) 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head) :
        if not head:
            return None
        pre = None
        cur = head 
        while cur:
            cur.next,pre,cur = pre,cur,cur.next
        return pre
        
# Approach #2 (Recursive)
class Solution:
    def reverseList(self, head):
        return self.helper(None,head)
    def helpfer(self,pre,cur):
        if cur:
            next_hop = cur.next
            cur.next = pre
            return self.helper(cur,next_hop)
        else:
            pre

        