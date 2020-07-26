'''
@Author: your name
@Date: 2020-05-23 13:02:49
@LastEditTime: 2020-05-23 13:43:55
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/Construct/106.Inorder_and_Postorder_Traversal.py
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution(object):
    def buildTree(self, inorder, postorder):
        self.inorder_map = {i:v for v,i in enumerate(inorder)}
        return self._buildTree(0, len(inorder)-1, postorder)

    def _buildTree(self, low, high, postorder):
        if low > high:
            return None
        
        root = TreeNode(postorder.pop())
        index = self.inorder_map[root.val]

        root.right = self._buildTree(index+1, high, postorder)
        root.left = self._buildTree(low, index-1, postorder)

        return root