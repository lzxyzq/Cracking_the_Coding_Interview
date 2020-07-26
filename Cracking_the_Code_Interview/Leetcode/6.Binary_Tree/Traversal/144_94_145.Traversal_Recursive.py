'''
@Author: your name
@Date: 2020-05-23 21:42:04
@LastEditTime: 2020-05-23 22:44:56
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/Traversal/144.Preorder_Traversal.py
'''
# Given a binary tree, return the preorder traversal of its nodes' values.
''' Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3] '''

class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
        
# Pre
class Solution():
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        res.append(root.val)
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))
        return res

# In 
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))
        return res


# Post
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        res.extend(self.postorderTraversal(root.left))
        res.extend(self.postorderTraversal(root.right))
        res.append(root.val)
        return res

if __name__ == '__main__':
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5)  
    print(Solution().postorderTraversal(root))
    