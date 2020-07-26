'''
@Author: your name
@Date: 2020-05-27 19:28:31
@LastEditTime: 2020-05-27 23:24:25
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/Traversal/226.Invert_Binary_Tree.py
'''
# Invert a binary tree.

''' Example:
Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1 
'''

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node and (node.left or node.right):
                node.left, node.right = node.right, node.left
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return root