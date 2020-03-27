# Write an algorithm to find the "next" node (i.e.in-order successor) of a given node in a binary search tree.You may assume that each node has a link to its parent.


class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inOrderSuccessor(root,n):
    if n.right:
        return minValue(n.right)
    
    p = n.parent
    while(p):
        # left node
        if n != p.right:
            break
        # right node find next root
        n = p
        p = p.parent
    return p 
          
def minValue(node): 
    
    current = node
    while (current):
        if not current.left:
            break
        current = current.left
    return current

def insert(node, data): 
  
    # 1) If tree is empty then return a new singly node 
    if node is None: 
        return Node(data) 
    else: 
         
        # 2) Otherwise, recur down the tree 
        if data <= node.data: 
            temp = insert(node.left, data) 
            node.left = temp  
            temp.parent = node 
        else: 
            temp = insert(node.right, data) 
            node.right = temp  
            temp.parent = node 
          
        # return  the unchanged node pointer 
        return node 

def inOrder(node): 
    if not node: 
        return
    inOrder(node.left) 
    print(node.data)
    inOrder(node.right)


if __name__ == '__main__':
# Creating the tree given in the above diagram  
#          20
#       8      22
#    4     12
#       10    14
#

    root = None 
    root = insert(root, 20) 
    root = insert(root, 8); 
    root = insert(root, 22); 
    root = insert(root, 4); 
    root = insert(root, 12); 
    root = insert(root, 10);   
    root = insert(root, 14); 
    print(inOrder(root))

    