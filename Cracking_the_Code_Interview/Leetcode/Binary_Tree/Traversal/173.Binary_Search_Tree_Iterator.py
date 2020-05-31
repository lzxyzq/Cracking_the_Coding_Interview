'''
@Author: your name
@Date: 2020-05-27 19:59:11
@LastEditTime: 2020-05-27 19:59:11
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/Traversal/173.Binary_Search_Tree_Iterator.py
'''
# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
# Calling next() will return the next smallest number in the BST.

''' Example:
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false 
'''
class BSTIterator:
    
    def __init__(self, root: TreeNode):
        self.values = []
        self.traverse(root)
        
    def traverse(self, node):
        """
        :type root: TreeNode
        """
        if not node:
            return
        self.traverse(node.left)
        self.values.append(node.val)
        self.traverse(node.right)

    def next(self):
        """
        @return the next smallest number
        """
        return self.values.pop(0)

    def hasNext(self) :
        """
        @return whether we have a next smallest number
        """
        if len(self.values):
            return True
        return False
