# Implement a function to check if a binary tree is balanced.For the purposes of this question,a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.


class TreeNode:
    def __init__(self,d,left = None ,right = None):
        self.data,self.left,self.right =d, left,right

def getDepth(root):
    if not root:
        return 0
    return max(getDepth(root.left),getDepth(root.right)) + 1 

def check_balance(root):
    if not root:
        return True
    if abs(getDepth(root.left) - getDepth(root.right)) > 1:
        return False
    return check_balance(root.left) and check_balance(root.right)
    
if __name__ == '__main__':
    root = TreeNode(1) 
    root.left = TreeNode(2) 
    root.right = TreeNode(3) 
    root.left.left = TreeNode(4) 
    root.left.right = TreeNode(5) 
    root.left.left.left = TreeNode(8) 
    print(check_balance(root))
    