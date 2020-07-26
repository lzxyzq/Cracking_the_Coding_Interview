'''
@Author: your name
@Date: 2020-06-16 10:54:53
@LastEditTime: 2020-06-17 11:13:26
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Singly_Linked_List/142.Linked_List_Cycle_II.py
'''
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Note: Do not modify the linked list.

# class Solution:
#     def detectCycle(self, head: ListNode):
#         runner = walker = head
#         while runner and runner.next:
#             runner = runner.next.next
#             walker = walker.next
#             if runner == walker:
#                 seeker = head
#                 while seeker != walker:
#                     walker = walker.next
#                     seeker = seeker.next
#                 return walker

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def _mergeLists(self,a, b):
    tail = a
    head = a
    a = a.next
    while b:
        tail.next = b
        tail = tail.next
        b = b.next
    if a:
        a, b = b, a      
    return head

def _reverseList(head):
    last = None
    currentNode = head
    while currentNode:
        currentNode.next = last
        last = currentNode
        currentNode = currentNode.next
    return last

def printList(node) : 
    while (node!=None):
        print(node.val,end=" ")
        node = node.next
a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
printList(a)

b = ListNode(5)
b.next = ListNode(4)
printList(b)

def _mergeLists(a, b):
    l1 = a 
    while (b):
        next = l1.next
        l1.next = b
        b = b.next
        l1.next.next = next 
        l1 = next 
_mergeLists(a,b)
printList(_reverseList(a))