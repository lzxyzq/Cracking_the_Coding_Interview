'''
@Author: your name
@Date: 2020-05-23 15:54:05
@LastEditTime: 2020-05-23 15:57:21
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/Construct/105.daf.py
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        self.inorder_map = {num:i for i,num in enumerate(inorder)}
        self.root_index = 0
        def helper(front,end):
            if front > end :
                return None
            root = TreeNode(preorder[self.root_index])
            self.root_index += 1
            index = self.inorder_map[root.val]
            root.left = helper(front, index-1)
            root.right = helper(index+1,end)
            return root
        return helper(0,len(inorder)-1)