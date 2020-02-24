# Return Kth to Last:Implement an algorithm to find the kth to last element of a singly linked list.

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


def kth_to_last(head, k):
    runner = current = head
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current
# Code execution starts here 
if __name__=='__main__': 
  
    head = None
    head = push(head, 80)  
    head = push(head, 13)  
    head = push(head, 80)  
    head = push(head, 70)  
    head = push(head, 11)  
    head = push(head, 11)  
    
    print("\nLinked list before ")  
    printList(head) 
    print("\nLinked list after ")  
    h = kth_to_last(head,2)
    printList(h)
    print("\n")