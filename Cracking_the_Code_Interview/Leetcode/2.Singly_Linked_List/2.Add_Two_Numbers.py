'''
@Author: your name
@Date: 2020-06-14 15:06:35
@LastEditTime: 2020-06-14 17:01:47
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Singly_Linked_List/2.Add_Two_Numbers.py
'''
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

''' Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        node1 = l1
        node2 = l2
        result_head,result_node = None,None
        carry = 0
        while node1 or node2 or carry:
            value = carry
            if node1:
                value += node1.val
                node1 = node1.next
            if node2:
                value += node2.val
                node2 = node2.next
            if result_node:
                result_node.next = ListNode(value % 10)
                result_node = result_node.next 
            else:
                result_node = ListNode(value % 10)
                result_head = result_node
            carry = value // 10
        return result_head

