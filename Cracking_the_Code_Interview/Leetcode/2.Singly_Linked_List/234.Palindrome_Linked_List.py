'''
@Author: your name
@Date: 2020-06-17 11:27:35
@LastEditTime: 2020-06-17 15:23:25
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Singly_Linked_List/234.Palindrome_Linked_List.py
'''
class Solution:
    def isPalindrome(self, head) :
        vals = []
        while head:
            vals += head.val,
            head = head.next
        return vals == vals[::-1]

class Solution:
    def isPalindrome(self, head) :
        fast = slow = head 
        # find the middle node 
        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        # reverse the second 
        pre = None 
        while slow:
            nxt = slow.next
            slow.next = pre 
            pre = slow 
            slow = nxt
        # compare the first and second half nodes
        while head:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next
        return True