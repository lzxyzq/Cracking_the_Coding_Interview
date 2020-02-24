# Delete Middle Node: Implement an algotithm to delete a node in the middle(i.e.any node but the first and last node,not necessarily the exact middle)of a singly linked list,given only access to that node.
# EXAMPLE
# Input:the node c from the linked list a -> b -> c -> d -> e -> f
# Result:nothing is returned,but the new linked list looks like a -> b -> d -> e -> f

class Node:
    def __init__(self,new_data,next=None):
        self.data = new_data
        self.next = next


def delete_middle(node):
    next = node.next
    node.data = next.data
    node.next = next.next
    return head

# Function to print nodes in a given linked list  
def printList(node) : 
    while (node!=None):
        print(node.data,end=" ")
        node = node.next
    

# Code execution starts here 
if __name__=='__main__': 
  
    head = Node(1,Node(2,Node(3,Node(4))))
    
    print("\nLinked list before ")  
    printList(head) 
    print("\nLinked list delete after ")  
    h = delete_middle(head.next.next)
    printList(h)
    print("\n")