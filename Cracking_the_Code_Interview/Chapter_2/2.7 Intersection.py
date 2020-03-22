# Given two linked lists, determine if the two lists intersect.Return the intersecting node.Note that the intersection is defined based on reference,not value.That is,if the kth node of the first linked list is the exact same node as the jth node of the second linked list,the they are intersecting.

class Node():
    def __init__(self, data, next=None):
        self.data, self.next = data, next

def intersection(head1, head2):
    nodes = {}
    node = head1
    while node:
        nodes[node] = True
        node = node.next
    node = head2
    while node:
        if node in nodes:
            return node
        node = node.next
    return None

def printList(node) : 
    if(node == None):
        print(None)
    while (node!=None):
        print(node.data,end=" ")
        node = node.next


if __name__=='__main__':    
    head1 = Node(10,Node(20,Node(30)))
    head2 = Node(20,Node(30,Node(40)))
    print("Linked list head1 before ")  
    printList(head1)
    print("\nLinked list head2 before ")  
    printList(head2)
    intersection_node = intersection(head1, head2)
    print("\nLinked list intersection after ")  
    printList(intersection_node)
    node = Node(70,Node(80))
    head3 = Node(50,Node(20,node))
    head4 = Node(60,Node(90,Node(10,node)))
    print("\nLinked list head3 before ")  
    printList(head3)
    print("\nLinked list head4 before ")  
    printList(head4)
    intersection_node_2 = intersection(head3, head4)
    print("Linked list intersection after ")  
    printList(intersection_node_2)
    print("\n")
    