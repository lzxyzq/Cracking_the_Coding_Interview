'''
@Author: your name
@Date: 2020-06-15 13:41:28
@LastEditTime: 2020-06-15 17:01:47
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Singly_Linked_List/61.Rotate List.py
'''
# Given a linked list, rotate the list to the right by k places, where k is non-negative.

''' Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''
class Solution:
    def rotateRight(self, head: ListNode, k: int) :
        if (not head or k == 0):
            return head
        length = 1
        p = head
        while (p.next):    # linked_list length
            length+=1
            p = p.next
        k = length - (k % length)
        
        p.next = head  # head tail connected
        for i in range(k):
            p=p.next
        head = p.next
        p.next = None
        return head 
        