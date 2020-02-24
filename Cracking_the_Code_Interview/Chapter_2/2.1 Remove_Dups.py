# Romove Dups:Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

# Recursion

# A linked list node
class Node:
    def __init__(self,new_data):
        self.data = new_data
        self.next = None

def push(head_ref, new_data):
    new_node = Node(0)
    new_node.data = new_data
    new_node.next = head_ref
    head_ref = new_node
    return head_ref

# Function to print nodes in a given linked list  
def printList(node) : 
    while (node!=None):
        print(node.data,end=" ")
        node = node.next

def removeDuplicates(head):
    # if head is None then return 
    if(head == None):
        return None

    # Remove duplicates from list after head 
    head.next = removeDuplicates(head.next)
    # check if head itself is duplicate
    if(head.next != None and head.next.data == head.data):
        res = head.next
        return res
    return head

def removeDuplicates_unsorted(head):
    if(head == None):
        return
    current = head
    while current:
        runner = current
        while runner.next:
            if (runner.next.data == current.data):
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return head

# Code execution starts here 
if __name__=='__main__': 
  
    # Start with the empty list 
    # llist = LinkedList() 
  
    # llist.head = Node(1) 
    # second = Node(2) 
    # third = Node(3) 
    # four = Node(4)
  
    # llist.head.next = second; # Link first node with second 
    # second.next = third; # Link second node with the third node 
    # third.next = four;
    # llist.printList() 
    head = None
    head = push(head, 80)  
    head = push(head, 13)  
    head = push(head, 80)  
    head = push(head, 70)  
    head = push(head, 11)  
    head = push(head, 11)  
    
    print("\nLinked list before duplicate removal ")  
    printList(head)  
    h = removeDuplicates(head)  
    print("\nLinked list after duplicate removal ")  
    printList(h)
    print("\nUnsorted Linked list after duplicate removal ")  
    unsorted_linked_list  = removeDuplicates_unsorted(head)
    printList(unsorted_linked_list)


  