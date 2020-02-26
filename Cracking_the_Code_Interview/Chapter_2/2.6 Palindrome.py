# Implement a function to check if a linked list is a palindrome.


class Node():
    def __init__(self, data, next=None):
        self.data, self.next = data, next

def is_palindrome(head):
    forward, backward = head, copy_reverse(head)
    while forward:
        if forward.data != backward.data:
            return False
        forward, backward = forward.next, backward.next
    return True

def copy_reverse(head):
    prev = None
    node = copy(head)
    while node:
        next = node.next
        node.next = prev
        prev = node
        node = copy(next)
    return prev

def copy(node):
    if node:
        return Node(node.data, node.next)
    else:
        return None


if __name__=='__main__':    
    list4 = Node(10,Node(70,Node(30,Node(70,Node(10)))))
    print(is_palindrome(list4))