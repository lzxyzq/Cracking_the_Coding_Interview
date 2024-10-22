'''
@Author: your name
@Date: 2020-06-14 12:23:36
@LastEditTime: 2020-06-14 16:16:23
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Singly_Linked_List/328.Odd Even Linked List.py
'''
# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

''' Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
'''
class Solution:
    def oddEvenList(self, head: ListNode):
        if (head == None):
            return None
        odd = head
        even = head.next 
        evenHead = even
        while(even and even.next):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head