# You have two numbers represented by a linked list ,where each node contains a single digit.The digits are stored i nreverse order,such that the 1's digit is at the head of the list.Write a function that adds the two numbers and returns the sum as a linked list.

#EXAMPLE 
#Input:(7 -> 1 -> 6) + (5 -> 9 -> 2).That is 617 + 295.
#Output:2 -> 1 -> 9. That is 912.
#FOLLOW UP 
#Suppose the digits are stored in forward order.Repeat the above problem.
#EXAMPLE 
#Input:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is 617 + 295.
#Output:9 -> 1 -> 2 .That is 912.

class Node:
    def __init__(self,new_data,next=None):
        self.data = new_data
        self.next = next

def printList(node) : 
    while (node!=None):
        print(node.data,end=" ")
        node = node.next

def sum_lists(num1, num2):
    node1, node2 = num1, num2
    carry = 0
    result_head, result_node = None, None
    while node1 or node2 or carry:
        value = carry
        if node1:
            value += node1.data
            node1 = node1.next
        if node2:
            value += node2.data
            node2 = node2.next
        if result_node:
            result_node.next = Node(value % 10)
            result_node = result_node.next
        else:
            result_node = Node(value % 10)
            result_head = result_node
        carry = value // 10
    return result_head



if __name__=='__main__': 
    num1 = Node(7,Node(1,Node(6)))
    num2 = Node(5,Node(9,Node(2)))
    total = sum_lists(num1, num2)
    print("\nLinked list 1 before ")  
    printList(num1)
    print("\nLinked list 2 before ")
    printList(num2)
    print("\nLinked list Sum List after ")  
    printList(sum_lists(num1, num2))