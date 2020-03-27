# Given a sorted array with unique integer elements,write an algorithm to create a binary search tree with minimal height(Balanced BST).

class BSTNode():
    def __init__(self, d):
        self.data, self.left, self.right = d, None, None

def minimal_height_bst(sorted_array):
    if not sorted_array:
        return None
    middle = len(sorted_array) // 2
    root = BSTNode(sorted_array[middle]) 
    root.left  = minimal_height_bst(sorted_array[:middle])
    root.right = minimal_height_bst(sorted_array[(middle+1):])
    return root
    
def preOrder(node): 
    if not node: 
        return
      
    print(node.data)
    preOrder(node.left) 
    preOrder(node.right)  

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7] 
    root = minimal_height_bst(arr) 
    print ("PreOrder Traversal of constructed BST") 
    preOrder(root) 
    