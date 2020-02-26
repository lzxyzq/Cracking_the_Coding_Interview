# Write code to partition a linked list around a value x,such that all nodes less than x come before all nodes greater than or equal to x.If x is contained within the list, the values of x only need to be after the elements less than x.The partition element x can appear anywhere in the "right partition";it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8 

class Node:
    def __init__(self,new_data,next=None):
        self.data = new_data
        self.next = next
def printList(node) : 
    while (node!=None):
        print(node.data,end=" ")
        node = node.next
def partition(node, x): 
    # Let us initialize start and 
    # tail nodes of new list  
    tail = node 
    # Now iterate original list  
    # and connect nodes 
    head = node 
    while (node != None): 
        next = node.next
        if (node.data < x):    
            # Insert node at head.  
            node.next = head 
            head = node 
        else: 
            # Append to the list of greater values 
            # Insert node at tail.  
            tail.next = node 
            tail = node 
        node = next
    tail.next = None
    # The head has changed, so we need 
    # to return it to the user. 
    return head 

if __name__=='__main__': 
  
    head = Node(3,Node(5,Node(8,Node(5,Node(10,Node(2,Node(1)))))))
    
    print("\nLinked list before ")  
    printList(head) 
    print("\nLinked list partition after ")  
    h = partition(head,x=5)
    printList(h)
    print("\n")