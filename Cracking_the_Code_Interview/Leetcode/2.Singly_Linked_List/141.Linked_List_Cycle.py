'''
@Author: your name
@Date: 2020-06-15 23:39:29
@LastEditTime: 2020-06-16 00:38:28
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Singly_Linked_List/141.Linked_List_Cycle.py
'''
# Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.


# 最容易想到的方法是，用一个哈希表unordered_map<int, bool> visited，记录每个元素是否被访问过，一旦出现某个元素被重复访问，说明存在环。空间复杂度O(n)，时间复杂度O(N)。

class Solution:
    def hasCycle(self, head: ListNode):
        hashset=set()
        while head:
            if head not in hashset: 
                hashset.add(head)
            else:
                return True
            head=head.next
        return False

# Follow up:
# Can you solve it using O(1) (i.e. constant) memory?
# 最好的方法是时间复杂度O(n)，空间复杂度O(1)的。设置两个指针，一个快一个慢，快的指针每次走两步，慢的指针每次走一步，如果快指针和慢指针相遇，则说明有环。
class Solution:
    def hasCycle(self, head: ListNode):
        slow = fast = head 
        while (fast and fast.next): # 如果fast.next为None None无next
            slow = slow.next
            fast = fast.next.next 
            if fast == slow :
                return True
        return False