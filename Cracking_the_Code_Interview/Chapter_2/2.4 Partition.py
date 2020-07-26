'''
@Author: your name
@Date: 2020-02-18 01:16:29
@LastEditTime: 2020-06-14 23:37:23
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Chapter_2/2.4 Partition.py
'''
# Write code to partition a linked list around a value x,such that all nodes less than x come before all nodes greater than or equal to x.If x is contained within the list, the values of x only need to be after the elements less than x.The partition element x can appear anywhere in the "right partition";it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# Output: 1 2 3 5 8 5 10  
# Leetcode 86 

class Node:
    def __init__(self,new_data,next=None):
        self.data = new_data
        self.next = next
def printList(node) : 
    while (node!=None):
        print(node.data,end=" ")
        node = node.next
def partition(self, head: Node, x: int) :
        temp1 = l1 = Node(0)
        temp2 = l2 = Node(0)
        while head:
            if head.val < x:
                temp1.next = Node(head.val)
                temp1 = temp1.next
            else:
                temp2.next = Node(head.val)
                temp2 = temp2.next
            head = head.next
        temp1.next = l2.next
        return l1.next

if __name__=='__main__': 
    head = Node(3,Node(5,Node(8,Node(5,Node(10,Node(2,Node(1)))))))
    print("\nLinked list before ")  
    printList(head) 
    print("\nLinked list partition after ")  
    h = partition(head,x=5)
    printList(h)
    print("\n")