'''
@Author: your name
@Date: 2020-05-31 21:33:50
@LastEditTime: 2020-06-01 01:42:47
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Array/82.Remove_Duplicates_from_Sorted_List_II.py
'''
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
# Return the linked list sorted as well.
''' 
Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def deleteDuplicates(head):
    prev = save_head = ListNode(0)
    save_head.next = head
    foundDuplicates = False
    
    while head and head.next:
        while head and head.next and head.val == head.next.val:
            foundDuplicates = True
            head = head.next
        if foundDuplicates:
            prev.next = head.next
            foundDuplicates = False
        else:
            prev = head
        head = head.next
        
    return save_head.next

def printList(temp):   
    while(temp):  
        print(temp.val , end = ' ') 
        temp = temp.next

if __name__ == '__main__':
    head = ListNode(11) 
    head.next = ListNode(12)
    head.next.next = ListNode(12)
    head.next.next.next = ListNode(14) 
    head.next.next.next.next = ListNode(15)
    printList(head)
    print("")
    deleteDuplicates(head)
    printList(head)
   