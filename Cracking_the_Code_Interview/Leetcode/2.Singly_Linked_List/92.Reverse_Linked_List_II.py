'''
@Author: your name
@Date: 2020-06-16 15:29:05
@LastEditTime: 2020-06-16 15:31:10
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Singly_Linked_List/92.Reverse_Linked_List_II.py
'''

# Reverse a linked list from position m to n. Do it in one-pass.
# Note: 1 ≤ m ≤ n ≤ length of list.

''' Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL 
'''

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    
    # Comparing with Problem 206: just need to find the start position 
    # then reverse (same as 206)
    
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        cur = dummy.next

        # find the position
        for i in range(1,m):
            cur = cur.next
            pre = pre.next
            
        # reverse
        for i in range(n-m):
            temp = cur.next
            cur.next = temp.next
            temp.next  = pre.next
            pre.next = temp

        return dummy.next